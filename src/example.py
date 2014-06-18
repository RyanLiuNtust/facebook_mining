from ml import *
from base import *
import sys, os
from os import listdir
from os.path import isfile, join

def ls(dir, ext, is_only_filename):
    files = []
    for file in os.listdir(dir):
        if file.endswith(ext):
            if(is_only_filename in ['true']):
                filename_extension_list = os.path.splitext(file)
                files.append(filename_extension_list[0])
            else:
                files.append(file)
    return files

def check_create_folder(dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

data_dir = "data/"
save_dir = "results/"
is_normalize = True

if len(sys.argv) < 2:
    sys.exit("Usage python %s data_dir/ save_dir/ (is_normalize)" % sys.argv[0])
elif len(sys.argv) == 4:
    is_normalize = sys.argv[3]
data_dir = sys.argv[1]
save_dir = sys.argv[2]

#filenames = ls(data_dir, "csv", "false")
filenames = ["all.csv"]
check_create_folder(save_dir)
for filename in filenames:
    name, ext = os.path.splitext(filename)
    src_name = data_dir + filename
    dst_name = save_dir + name + ".png"
    database = load_like_comment(src_name)
    n_clusters = 3
    if len(database.data) > n_clusters:
       unnorm_data = database.data
       norm_data = get_normed_data(unnorm_data, [0.4, 0.6], norm_policy.NORM)
       draw_kmeans(norm_data, n_clusters, database.target_gender, dst_name)
