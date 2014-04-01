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

#friend_status_info_dict
#id:[message, likes] or [message, likes, comments] depend on whether the comment is exist
def get_status_info(friendlist_status):
    print "get likes info about statuses...."
    friend_status_info_dict = dict()
    total_statuses = len(friendlist_status)
    current_person_status = 1
    for author_id, status in friendlist_status:
        print "%d/%d...." %(current_person_status, total_statuses)
        friend_status_info_dict[author_id] = []
        for post in status:
            if 'message' in post and 'likes' in post and 'comments' in post:
                val = {'message':post['message'], 'likes':post['likes'], 'comments':post['comments']}
            elif 'message' in post and 'likes' in post:
                val = {'message':post['message'], 'likes':post['likes']}
            friend_status_info_dict = addData2Dict(author_id, val, friend_status_info_dict)
        current_person_status += 1
    return friend_status_info_dict

def heterosexual_post(posts, id_gender_dict):
    print "mining statuses....."
    total_post = len(posts)
    current_person_post = 1
    for key in posts.keys():
        print "%d/%d" %(current_person_post, total_post)
        author_id = key
        opp_gender = get_heterosexual(id_gender_dict[author_id])
        for post_msg in posts[key]:
            if 'message' in post_msg and 'likes' in post_msg:
                print 'message: \n%s' %(post_msg['message'])
                print 'like: \n%s' %(post_msg['likes']['data'])
            if 'comments' in post_msg:
                print 'comment:\n %s' %(post_msg['comments']['data'])
        current_person_post += 1
        print "id: %s total_post %s" %(author_id, len(posts[key]))


