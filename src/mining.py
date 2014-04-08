#version 0.1
#Author RyanLiuNtust
#Time 3/29
import os, sys, facebook
lib_path = os.path.abspath('./../include/')
sys.path.append(lib_path)
from fbGrepper import *
from facebook_mining import *
auth_access_token = "CAACEdEose0cBAFUKtAGOoOTvEZBISe7ieNdwRUWYI3VLOPJeZCZAxi4ToeTZCHDtiz0gYtVZAqhiEnCLxip1SpC9CdCyxkYYrPZBwSyU2WjQ06ato4Y6buH5KXoXmJEtZAWwdocCAUGpIWRzmEnUBi0DR1rIG2HN0HgkYAMxNLy1D4nJ7weqvrZC26yVua4VtoQZD"

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    #print cvtDict2Chinese(friends)
    #feed = get_my_feed(graph)
    #print cvtDict2Chinese(feed)
    friendlist_status = get_my_friends_status(graph, friends, 51)
    #print cvtDict2Chinese(friendlist_status)
    likes_dict = get_status_info(friendlist_status)
    heterosexual_post(likes_dict, get_my_friends_gender(get_my_friends_about(graph, friends)), graph)
    #print cvtDict2Chinese(likeslist)
    #friendlist_about = get_my_friends_about(graph, friends)
    #for about in friendlist_about:
    #    if 'gender' in about:
    #        print about["name"] + " " + about["gender"]

if __name__ == "__main__":
    main()

