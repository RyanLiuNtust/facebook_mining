#version 0.1
#Author RyanLiuNtust
#Time 3/31

import facebook
import sys
import csv
DEBUG_MODE = False

def enum(**enums):
    return type('Enum', (), enums)

FRIEND_INFO = enum(ABOUT = 'about', STATUSES = 'statuses')

def get_my_friends(graph):
    print "get friends info...."
    friendlist = graph.get_connections('me', 'friends')['data']
    friends = [(friend['id'], friend['name'],) for friend in friendlist]
    print 'total of friend = %d\n' %len(friends)
    return friends

def get_my_feed(graph):
    print "get my feed...."
    feed_dict = graph.get_connections('me', 'feed')['data']
    return feed_dict

def cvtDict2Chinese(dict):
    return str(dict).decode('unicode-escape')

#create a list of dict to save multiple dict with same key
def get_my_friends_about(graph, friends):
    print "get friend about info...."
    friendlist_profile = []
    total_friend = len(friends)
    current_friend = 1
    for friend in friends:
        print "%d/%d....." %(current_friend, total_friend)
        friendlist_profile.append(graph.get_object(friend[0]))
        current_friend += 1
        if(DEBUG_MODE):
            break
    return friendlist_profile

#statuses is defined that you post on your own wall
#friendlist_status save as [id, status_list corresponding to id]
def get_my_friends_status(graph, friends, limit_num_status = None):
    print "get friends statuses...."
    if limit_num_status is None:
        limit_num_status = 25
    friendlist_status = []
    total_friend = len(friends)
    current_friend = 1
    for friend in friends:
        print "%d/%d....." %(current_friend, total_friend)
        id = friend[0]
        statuses = graph.get_connections(id, 'statuses', limit = limit_num_status)['data']
        friendlist_status.append((id, statuses))
        current_friend += 1
        if(DEBUG_MODE):
            if current_friend == 2:
		    	break
    return friendlist_status

def get_my_friends_gender(friendlist_profile):
    print "get friend gender info...."
    id_gender_dict = dict()
    current_about = 1
    total_about = len(friendlist_profile)
    for about in friendlist_profile:
        print "%d/%d....." %(current_about, total_about)
        if 'gender' in about:
            id_gender_dict[about['id']] = about['gender']
        else:
            id_gender_dict[about['id']] = "non"
        current_about += 1
        if(DEBUG_MODE):
            if current_about == 2:
                break
    return id_gender_dict
