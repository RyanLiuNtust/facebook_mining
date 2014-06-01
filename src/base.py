import csv

import numpy as np
class Bunch(dict):

    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)
        self.__dict__ = self

def load_like_comment(filename):
    """""Load and return the heterosexual's all likes and comments corresponding to author

    ==============================================================
    ||     data        ||  source ||          target            ||
       likes   comments   hex_ID    target_id(author_ID)  gender
    ==============================================================
    Examples
    """""
    with open(filename) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_hex = int(temp[0])
        n_features = int(temp[1])
        target_id = int(temp[2])
        target_gender = temp[3]
        data = np.empty((n_hex, n_features))
        hex_id = np.empty((n_hex,), dtype=np.int)

        for i, info in enumerate(data_file):
            hex_id[i] = np.asarray(info[0], dtype=np.int)
            data[i] = np.asarray(info[1:], dtype=np.int)
    return Bunch(data=data, hex_id=hex_id,
                 target_id=target_id,
                 target_gender=target_gender)


    
