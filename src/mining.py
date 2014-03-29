#version 1.0
#Author RyanLiuNtust
#Time 3/29
import os, sys, facebook
lib_path = os.path.abspath('./../include/')
sys.path.append(lib_path)
from fbGrepper import *

auth_access_token = "CAACEdEose0cBAFIXvicm4FDIwjxFticxgZAFD6QW3yQpgN90ZASKwel5w78ZCEbmGlM7yyEXva1BDNHlaFjoMAEC8Ll3SSyyXyZAljTqwrC0KT8n94OfP9zWNMJhA7ZAxvE2tjMN2L6ZAGDVOv7wbxViMqr8agNQ8cCWaxUQK4FtCS1mIs2q7uCqflS41vNlEZD"

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    print friends
    feed = get_my_feed(graph)
    print feed

    friendlist_about = get_my_friends_about(graph, friends)
    for about in friendlist_about:
        if 'gender' in about:
            print about["name"] + " " + about["gender"]

if __name__ == "__main__":
    main()

