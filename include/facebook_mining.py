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

#friend_status_info_dict format is following:
#author_id:[message_id, likes] or [message_id, likes, comments] depend on whether the comment is exist
def get_status_info(friendlist_status):
    print "get likes info about statuses...."
    friend_status_info_dict = dict()
    total_statuses = len(friendlist_status)
    current_person_status = 1
    for author_id, status in friendlist_status:
        print "%d/%d...." %(current_person_status, total_statuses)
        friend_status_info_dict[author_id] = []
        for post in status:
            if 'likes' in post and 'comments' in post:
                val = {'post_id':post['id'], 'likes':post['likes'], 'comments':post['comments']}
            elif 'likes' in post:
                val = {'post_id':post['id'], 'likes':post['likes']}
            friend_status_info_dict = addData2Dict(author_id, val, friend_status_info_dict)
        current_person_status += 1
    return friend_status_info_dict

#heterosexual_post format is following:
#{author_id:['message_id(1)':{'likes_id':[heterosexual_ids], 'commen_ids':[heterosexual_ids]}, 
#            'message_id(2)':{'likes_id':[heterosexual_ids], 'commen_ids':[heterosexual_ids]},.....]}
def heterosexual_post(posts, id_gender_dict, graph):
    print "mining statuses....."
    total_person_post = len(posts)
    current_person_post = 1
    heterosexual_post = dict()
    for key in posts.keys():
        print "person %d/%d" %(current_person_post, total_person_post)
        author_id = key
        opp_gender = get_heterosexual(id_gender_dict[author_id])
        heterosexual_post[author_id] = []
        total_post = len(posts[author_id])
        current_post = 1
        for post_msg in posts[author_id]:
            print "%d/%d....." %(current_post, total_post)
            heterosexual_likeslist = []
            heterosexual_commentlist = []
            post_id = post_msg['post_id']
            if 'likes' in post_msg:
                likes = post_msg['likes']['data']
                for obj in likes:
                    obj_id = obj['id']
                    obj_profile = graph.get_object(obj_id)
                    if 'gender' in obj_profile and obj_profile['gender'] == opp_gender:
                        heterosexual_likeslist.append(obj_id)
            if 'comments' in post_msg:
                comments = post_msg['comments']['data']
                for obj in comments:
                    obj_id = obj['from']['id']
                    obj_profile = graph.get_object(obj_id)
                    if 'gender' in obj_profile and obj_profile['gender'] == opp_gender:
                        heterosexual_commentlist.append(obj_id)
            val = {post_id:{'like_ids':heterosexual_likeslist, 'comment_ids':heterosexual_commentlist}}
            addData2Dict(author_id, val, heterosexual_post)
            print 'like size %d, ids %s' %(len(heterosexual_post[author_id][current_post-1][post_id]['like_ids']), heterosexual_post[author_id][current_post-1][post_id]['like_ids'])
            print 'comment size %d, ids %s' %(len(heterosexual_post[author_id][current_post-1][post_id]['comment_ids']),heterosexual_post[author_id][current_post-1][post_id]['comment_ids'])
            current_post += 1
        current_person_post += 1
        print "author_id: %s total_post %s" %(author_id, len(posts[key]))
    print heterosexual_post
    return heterosexual_post


