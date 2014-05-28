from ml import *
from base import *
import sys, os
from os import listdir
from os.path import isfile, join

def ls(dir, ext, is_only_filename):
    files = []
    print is_only_filename
    for file in os.listdir(dir):
        if file.endswith(ext):
            if(is_only_filename in ['true']):
                filename_extension_list = os.path.splitext(file)
                files.append(filename_extension_list[0])
            else:
                files.append(file)
    return files

data_dir = "data/"
save_dir = "result/"
filenames = ls(data_dir, "csv", "false")

for filename in filenames:
    name, ext = os.path.splitext(filename)
    src_name = data_dir + filename
    dst_name = save_dir + name + ".png"
    database = load_like_comment(src_name)
    n_clusters = 3
    if len(database.data) > n_clusters:
       draw_kmeans(database.data, n_clusters, dst_name)
