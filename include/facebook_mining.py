#Version 0.1
#Author RyanLiuNtust
#Time 3/31
import os, sys, facebook
 
lib_path = os.path.abspath('./')
sys.path.append(lib_path)
def get_heterosexual(gender):
    if gender == 'male':
        return 'female'
    else:
        return 'male'

def addData2Dict(key, val, dict):
    if not key in dict:
        dict[key] = []
    dict[key].append(val)
    return dict

#friend_like_dict
#id:[message, likes]
def get_likes(friendlist_status):
    print "get likes info about statuses...."
    friend_like_dict = {}
    total_statuses = len(friendlist_status)
    current_status = 1
    for s in friendlist_status:
        print "%d/%d...." %(current_status, total_statuses)
        author_id = s[0]
        status = s[1]
        friend_like_dict[author_id] = []
        for post in status:
            if 'message' in post and 'likes' in post:
                #save nessage for testing,and consider whether the corresponding comment need to be saved
                val = (post['message'], post['likes'])
                friend_like_dict = addData2Dict(author_id, val, friend_like_dict)
                #print len(friend_like_dict)
        current_status += 1
    return friend_like_dict

def heterosexual_post(posts, id_gender_dict):
    print "mining statuses....."
    total_post = len(posts)
    current_post = 1
    for key in posts.keys():
        print "%d/%d" %(current_post, total_post)
        author_id = key
        opp_gender = get_heterosexual(id_gender_dict[author_id])
        #print "post %s" %posts[key]
        current_post += 1
