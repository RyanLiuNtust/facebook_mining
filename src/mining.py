#version 0.1
#Author RyanLiuNtust
#Time 3/29
import os, sys, facebook
lib_path = os.path.abspath('./../include/')
sys.path.append(lib_path)
from fbGrepper import *
from facebook_mining import *
auth_access_token = "CAACEdEose0cBAF8BlEAh7q6RrYIvcZC0jkwZBgBZAAaAhmRc0XFnHiew8KDD6UzDckGhGK1sWKvjBLA3trZChUodaZACWGcz0h8XrLdML3etOdb56tyZAq2dfrFaqPfVx4Xm7xCDZBbionABDexG6dmI0PqhxZCHIV1g76IYim75esCgT6o9XbzUXPeFZAy3j7XwZD"

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    #print cvtDict2Chinese(friends)
    #feed = get_my_feed(graph)
    #print cvtDict2Chinese(feed)
    friendlist_status = get_my_friends_status(graph, friends)
    #print cvtDict2Chinese(friendlist_status)
    likes_dict = get_likes(friendlist_status)
    heterosexual_post(likes_dict, get_my_friends_gender(get_my_friends_about(graph, friends)))
    #print cvtDict2Chinese(likeslist)
    print 'length = %d' %len(likes_dict)
    for likes in likes_dict:
		print "likeslist..........\n"
		print likes
    #friendlist_about = get_my_friends_about(graph, friends)
    #for about in friendlist_about:
    #    if 'gender' in about:
    #        print about["name"] + " " + about["gender"]

if __name__ == "__main__":
    main()

