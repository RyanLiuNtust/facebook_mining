from base import load_like_comment
from matplotlib import pyplot
import numpy as np
from sklearn import cluster
from matplotlib.patches import Ellipse

class norm_policy(object):
    NORM, STD_NORM, RANGE_NORM, NONE = range(4)

def normalize(data):
    data = data.astype(np.float32, copy=False)
    max = np.max(data)
    min = np.min(data)
    if (max-min) != 0:
        return (data-min)/(max-min)
    else:
        return data

def std_normalize(data):
    data = data.astype(np.float32, copy=False)
    mean = np.mean(data)
    var = np.var(data)
    if var != 0:
        return (data-mean)/var
    else:
        return data

def std_mean_normalize(data):
    data = data.astype(np.float32, copy=False)
    mean = np.mean(data)
    max_range = np.max(data) - np.min(data)
    if max_range != 0:
        return (data-mean)/max_range
    else:
        return data

def draw_circle(fig, center, radius):
    circle = pyplot.Circle(center, radius=radius, fc='b', fill=False)
    fig.gca().add_artist(circle)

def plot_point_cov(points, nstd=2, ax=None, **kwargs):
    """
    Plots an `nstd` sigma ellipse based on the mean and covariance of a point
    "cloud" (points, an Nx2 array).

    Parameters
    ----------
        points : An Nx2 array of the data points.
        nstd : The radius of the ellipse in numbers of standard deviations.
            Defaults to 2 standard deviations.
        ax : The axis that the ellipse will be plotted on. Defaults to the 
            current axis.
        Additional keyword arguments are pass on to the ellipse patch.

    Returns
    -------
        A matplotlib ellipse artist
    """
    pos = points.mean(axis=0)
    cov = np.cov(points, rowvar=False)
    return plot_cov_ellipse(cov, pos, nstd, ax, **kwargs)

def plot_cov_ellipse(cov, pos, nstd=2, ax=None, **kwargs):
    """
    Plots an `nstd` sigma error ellipse based on the specified covariance
    matrix (`cov`). Additional keyword arguments are passed on to the 
    ellipse patch artist.

    Parameters
    ----------
        cov : The 2x2 covariance matrix to base the ellipse on
        pos : The location of the center of the ellipse. Expects a 2-element
            sequence of [x0, y0].
        nstd : The radius of the ellipse in numbers of standard deviations.
            Defaults to 2 standard deviations.
        ax : The axis that the ellipse will be plotted on. Defaults to the 
            current axis.
        Additional keyword arguments are pass on to the ellipse patch.

    Returns
    -------
        A matplotlib ellipse artist
    """
    def eigsorted(cov):
        vals, vecs = np.linalg.eigh(cov)
        order = vals.argsort()[::-1]
        return vals[order], vecs[:,order]

    if ax is None:
        ax = pyplot.gca()

    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
    
    # Width and height are "full" widths, not radius
    width, height = 2 * nstd * np.sqrt(vals)
    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, color='y', fill=False, **kwargs)
    ax.add_artist(ellip)
    print "angle = " + str(theta)
    print "pos= " + str(pos) + " w = " + str(width) + " h = " + str(height)
    return (ellip, width, height)

# will fail when the elipse is oblique
def multi_gauss_outlier(data, var_x, var_y):
    indexs = []
    mean_x = data[:,0].mean()
    mean_y = data[:,1].mean()
    print "mean_x = " + str(mean_x) + " mean_y = " + str(mean_y)
    for index, d in enumerate(data):
        # (x-h)^2/rx%2 + (y-k)^2/ry^2 <= 1
        if ((d[0]-mean_x)**2/var_x**2 + (d[1]-mean_y)**2/var_y**2) <= 1:
            continue
        indexs.append(index)
    return indexs

#ORC refer to http://cs.joensuu.fi/~villeh/35400978.pdf
def outlier_removal_clustering(data, threshold):
    centroid = np.mean(data)
    dist = np.abs(data - centroid)
    dist_max = np.max(dist)
    outlyingness = dist/dist_max
    return np.where(outlyingness > threshold)[0]

def get_normed_data(data, weight, npolicy):
    data[:, 0] = weight[0] * data[:, 0]
    data[:, 1] = weight[1] * data[:, 1]

    if npolicy == norm_policy.NORM:
        data[:, 0] = normalize(data[:, 0])
        data[:, 1] = normalize(data[:, 1])

    elif npolicy == norm_policy.STD_NORM:
        data[:, 0] = std_normalize(data[:, 0])
        data[:, 1] = std_normalize(data[:, 1])

    elif npolicy == norm_policy.RANGE_NORM:
        data[:, 0] = std_mean_normalize(data[:, 0])
        data[:, 1] = std_mean_normalize(data[:, 1])

    return data

def draw_kmeans(data, n_cluster, author_gender, save_fig_name):
    is_find_outlier = True

    max_x = np.max(data[:,0])
    max_y = np.max(data[:,1])
    legend_x = max_x/3
    legend_y = max_y/3
    min_xlim = -max_x/10
    min_ylim = -max_y/10
    max_xlim = max_x + legend_x
    max_ylim = max_y + legend_y
    number_of_person = len(data)
    mark_shape = ['o', '^', 's', '*']
    mark_color = ['b', 'g', 'r', 'y']
    mark_labels = ['low', 'medium', 'high', 'outlier']

    kmeans = cluster.KMeans(n_clusters=n_cluster)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    for i, sorted_index in enumerate(np.argsort(centroids[:,1])):
        original_indexs = np.where(labels==sorted_index)
        ds = data[original_indexs]
        pyplot.plot(ds[:,0], ds[:,1], mark_shape[i], color=mark_color[i], label=mark_labels[i])
        #elipse, width, height = plot_point_cov(ds[:,:])
        if mark_labels[i] == 'high':
            elipse, width, height = plot_point_cov(ds[:,:])
            if is_find_outlier:
                indexs = outlier_removal_clustering(ds, 0.6)
                
            #    indexs = multi_gauss_outlier(ds[:,:], width/2.0, height/2.0)
                pyplot.plot(ds[indexs,0], ds[indexs,1], mark_shape[3], color=mark_color[3], label=mark_labels[3])
                print "outlier(original indexs):", original_indexs[0][indexs]
                print data[original_indexs[0][indexs]]
        lines = pyplot.plot(centroids[sorted_index,0], centroids[sorted_index,1], 'kx', color=mark_color[i])
        pyplot.setp(lines, ms=10.0)
        pyplot.setp(lines, mew=2.0)

    title = "The closeness based on kmeans (" + str(number_of_person) + " persons)"
    #title = "The closeness based on kmeans (" + author_gender + ")"
    pyplot.title(title, fontsize = 20)
    pyplot.grid(True)
    pyplot.xlabel('likes', fontsize = 16)
    pyplot.ylabel('comments', fontsize = 16)
    pyplot.xlim([0,max_xlim])
    pyplot.ylim([min_ylim,max_ylim])
    legend = pyplot.legend(numpoints=1,title='Closeness', loc=4, shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    if save_fig_name:
        pyplot.savefig(save_fig_name)
        print "The figuare save as", save_fig_name
    pyplot.clf()
