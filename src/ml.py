from base import load_like_comment
from matplotlib import pyplot
import numpy as np
from sklearn import cluster
from matplotlib.patches import Ellipse
def normalize(data):
    data = data.astype(np.float32, copy=False)
    max = np.max(data)
    min = np.min(data)
    if (max-min) != 0:
        return (data-min)/(max-min)
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
    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, fill=False, **kwargs)
    print width
    print height
    ax.add_artist(ellip)
    return ellip

def draw_kmeans(data, n_cluster, author_gender, save_fig_name, weight, is_normalize):
    legend_x = 10
    legend_y = 5
    if is_normalize == "True":
        data[:, 0] = weight[0] * data[:, 0]
        data[:, 1] = weight[1] * data[:, 1]
        data[:, 0] = normalize(data[:, 0])
        data[:, 1] = normalize(data[:, 1])
        legend_x = 0.5
        legend_y = 0.1
    min_ylim = -0.2
    max_xlim = np.max(data[:,0]) + legend_x
    max_ylim = np.max(data[:,1]) + legend_y
    number_of_person = len(data)
    mark_shape = ['o', '^', 's', '*']
    mark_color = ['b', 'g', 'r', 'y']
    mark_labels = ['low', 'medium', 'high', 'highest']
    kmeans = cluster.KMeans(n_clusters=n_cluster)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_


    for i, sorted_index in enumerate(np.argsort(centroids[:,0])):
        ds = data[np.where(labels==sorted_index)]
        pyplot.plot(ds[:,0], ds[:,1], mark_shape[i], color=mark_color[i], label=mark_labels[i])
        if mark_labels[i] == 'high':
            plot_point_cov(ds[:,:])
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
        print 'The figuare save as ' + save_fig_name
        pyplot.savefig(save_fig_name)
    pyplot.clf()
