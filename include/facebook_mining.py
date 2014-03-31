import os, sys, facebook
 
lib_path = os.path.abspath('./')
sys.path.append(lib_path)
def get_heterosexual(gender):
    if gender == 'male':
        return 'female'
    else:
        return 'male'

def addData2Dict(key, val, dict):
    value = []
    #need to check whether the type of val is list
    if not isinstance(val, list):
        value = [val]
    else:
        value = val
    if not key in dict:
        dict[key] = value
    else:
        dict[key].append(value)

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
        friend_like_dict = {author_id:[]}
        for post in status:
            if 'message' in post and 'likes' in post:
                #save nessage for testing,and consider whether the corresponding comment need to be saved
                val = [post['message'], post['likes']]
                print 1
                addData2Dict(author_id, val,  friend_like_dict)
        current_status += 1
    return friend_like_dict

def heterosexual_post(posts, genderlist):
    print "mining statuses....."
    total_post = len(posts)
    current_post = 1
    for post in posts:
        print "%d/%d" %(current_post, total_post)
        author_id = post.keys()
        opp_gender = get_heterosexual(author_id)
        
