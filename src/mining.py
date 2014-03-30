#version 1.0
#Author RyanLiuNtust
#Time 3/29
import os, sys, facebook
lib_path = os.path.abspath('./../include/')
sys.path.append(lib_path)
from fbGrepper import *

auth_access_token = "CAACEdEose0cBAAiniVjzuSvc3nN24ZAicYuVMTLADiZB1S5fYPqBe24XqSk0BEbndg2lF9AxseuFD2tjraLJOoBCZATledOvIMDqbeFfSNCnPF9qtnBT70FRv371mUPIhb6UZC8ef8j8NOvitkkl4YanHXJI0qLv7GBZAPZBzn63gW3ZCSEKA8etJeE3IN9QcyYc7YcmzGEYgZDZD"

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    #print cvtDict2Chinese(friends)
    #feed = get_my_feed(graph)
    #print cvtDict2Chinese(feed)
    friendlist_status = get_my_friends_status(graph, friends)
    print cvtDict2Chinese(friendlist_status)
    likeslist = get_likes(friendlist_status)
    print 'likeslist'
    print cvtDict2Chinese(likeslist)
    #friendlist_about = get_my_friends_about(graph, friends)
    #for about in friendlist_about:
    #    if 'gender' in about:
    #        print about["name"] + " " + about["gender"]

if __name__ == "__main__":
    main()

