#version 0.1
#Author RyanLiuNtust
#Time 3/29
import os, sys, facebook
lib_path = os.path.abspath('./../include/')
sys.path.append(lib_path)
from fbGrepper import *
from facebook_mining import *
auth_access_token = "CAACEdEose0cBANBKROvR7JVgNji1MMjWJGRZAIodnZAStFATr400Hs8Rm9CaUL9Q53PvfS23Km5T6XSNrWWVmXfZB6rnrCmMSHMcHZB2P4S36RfnXquNkT3fjxiaZB73IYZBM0tfB6r2WG98Il2deFdVZBR6851mEP36rY4JrFD99S6lDrGTIWaP6IoXskbQmgZD"

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    #print cvtDict2Chinese(friends)
    #feed = get_my_feed(graph)
    #print cvtDict2Chinese(feed)
    friendlist_status = get_my_friends_status(graph, friends)
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

