#version 0.1
#Author RyanLiuNtust
#Time 3/29
import os, sys, facebook
from os import listdir
from os.path import isfile, join
lib_path = os.path.abspath('./../include/')
sys.path.append(lib_path)
from fbGrepper import *
from facebook_mining import *

auth_access_token = "CAACEdEose0cBAMnzZBU0Crf4wKynsK1rV5h2yZCNXv3oiH0pTMat9suJZCKeHHsaWGKsNpFPwyayK44pEF3W2a8O67QmjVbNkZAXLiNeZCSfXuF2uVkcoKS5lSA9d2xS0yotoN2fjcZAXqaqDX1PrKp5FvjgIlv8NVAbVWC7PTdrBRjcEvUZAWBQX3UufsCFAWQqLOhW9JhZBAZDZD"

def ls(dir, ext, is_only_filename = False):
    files = []
    for file in os.listdir(dir):
        if file.endswith(ext):
            if(is_only_filename):
                filename_extension_list = os.path.splitext(file)
                files.append(filename_extension_list[0])
            else:
                files.append(file)
    return files

def get_snapshot(snapshot):
    snapshot.sort(key=int,reverse=True)
    return int(snapshot[0])

def main():
    save_csv_dir = "./csv/"
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    files = ls(save_csv_dir, 'csv', True)
    #print cvtDict2Chinese(friends)
    #feed = get_my_feed(graph)
    #print cvtDict2Chinese(feed)
    friendlist_status = get_my_friends_status(graph, friends, 50)
    #print cvtDict2Chinese(friendlist_status)
    likes_dict = get_status_info(friendlist_status)
    heterosexual_post(likes_dict, get_my_friends_gender(get_my_friends_about(graph, friends)), graph, get_snapshot(files))
    #print cvtDict2Chinese(likeslist)
    #friendlist_about = get_my_friends_about(graph, friends)
    #for about in friendlist_about:
    #    if 'gender' in about:
    #        print about["name"] + " " + about["gender"]

if __name__ == "__main__":
    main()

