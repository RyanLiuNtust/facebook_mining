from base import load_like_comment
from matplotlib import pyplot
import numpy as np
from sklearn import cluster
def normalize(data):
    data = data.astype(np.float32, copy=False)
    max = np.max(data)
    min = np.min(data)
    if (max-min) != 0:
        return (data-min)/(max-min)
    else:
        return data

def draw_kmeans(data, n_cluster, author_gender, save_fig_name, weight, is_normalize):
    legend_x = 10
    if is_normalize == True:
        data[:, 0] = weight[0] * data[:, 0]
        data[:, 1] = weight[1] * data[:, 1]
        data[:, 0] = normalize(data[:, 0])
        data[:, 1] = normalize(data[:, 1])
        legend_x = 0.5
    max_xlim = np.max(data[:,0]) + legend_x
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
        lines = pyplot.plot(centroids[sorted_index,0], centroids[sorted_index,1], 'kx', color=mark_color[i])
        pyplot.setp(lines, ms=10.0)
        pyplot.setp(lines, mew=2.0)

    #title = "The clossness based on kmeans (all)"
    title = "The clossness based on kmeans (" + author_gender + ")"
    pyplot.title(title, fontsize = 20)
    pyplot.grid(True)
    pyplot.xlabel('likes', fontsize = 16)
    pyplot.ylabel('comments', fontsize = 16)
    pyplot.xlim([0,max_xlim])
    legend = pyplot.legend(numpoints=1,title='Clossness', loc=4, shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    if save_fig_name:
        print 'The figuare save as ' + save_fig_name
        pyplot.savefig(save_fig_name)
    pyplot.clf()
