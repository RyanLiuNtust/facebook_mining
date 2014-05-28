from base import load_like_comment
from matplotlib import pyplot
import numpy as np
from sklearn import cluster

def draw_kmeans(data, n_cluster, save_fig_name):
    kmeans = cluster.KMeans(n_clusters=n_cluster)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    for i in range(n_cluster):
        ds = data[np.where(labels==i)]
        pyplot.plot(ds[:,0], ds[:,1], 'o')

        lines = pyplot.plot(centroids[i,0], centroids[i,1], 'kx')
        pyplot.setp(lines, ms=15.0)
        pyplot.setp(lines, mew=2.0)
    if save_fig_name:
        print 'The figuare save as ' + save_fig_name
        pyplot.savefig(save_fig_name)
    pyplot.clf()
