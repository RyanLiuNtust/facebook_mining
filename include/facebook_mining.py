#Version 0.1
#Author RyanLiuNtust
#Time 3/31
import os, sys, facebook, csv
 
lib_path = os.path.abspath('./')
sys.path.append(lib_path)
def get_heterosexual(gender):
    if gender == 'male':
        return 'female'
    else:
        return 'male'

def add_val_dictlist(key, val, dict):
    if not key in dict:
        dict[key] = []
    dict[key].append(val)
    return dict

def wrt_heterosexual_info(author_id, author_gender, heterosexual_dict, filename):
    f = open(filename, 'wb')
    f.write('author_id:' + str(author_id) + ',author_gender,' + str(author_gender) + '\n')
    for id in heterosexual_dict.keys():
        f.write(id + ',likes,' + str(len(heterosexual_dict[id]['likes'])))
        for time in heterosexual_dict[id]['likes']:
            f.write(',' + str(time))
        f.write(',comments,' + str(len(heterosexual_dict[id]['comments'])))
        for time in heterosexual_dict[id]['comments']:
            f.write(',' + str(time))
        f.write('\n')
    f.write('\n')
    f.close()

def calulate_like_comment(heterosexual_post, limit):
    heterosexual_dict = dict()
    for author_id in heterosexual_post.keys():
        print len(heterosexual_post[author_id])
        for msg in heterosexual_post[author_id]:
            updated_time = msg['updated_time']
            for like_id in msg['like_ids']:
                if like_id not in heterosexual_dict:
                    heterosexual_dict[like_id] = {'likes':[], 'comments':[]}
                heterosexual_dict[like_id]['likes'].append(updated_time)

            for comment_data in msg["comment_datas"]:
                comment_id = comment_data['comment_id']
                comment_time = comment_data['comment_time']
                if comment_id not in heterosexual_dict:
                    heterosexual_dict[comment_id] = {'likes':[], 'comments':[]}
                heterosexual_dict[comment_id]['comments'].append(comment_time)

            for id in heterosexual_dict.keys():
                print 'post_author_id = %s' %id
                for time in heterosexual_dict[id]['likes']:
                    print 'likes = %s' %time
                for time in heterosexual_dict[id]['comments']:
					print 'created_time = %s' %time
    return heterosexual_dict

#friend_status_info_dict format is following:
#author_id:[message_id, likes] or [message_id, likes, comments] depend on whether the comment is exist
def get_status_info(friendlist_status):
    print "mining likes info about statuses...."
    friend_status_info_dict = dict()
    total_statuses = len(friendlist_status)
    current_person_status = 1
    for author_id, status in friendlist_status:
        print "%d/%d...." %(current_person_status, total_statuses)
        friend_status_info_dict[author_id] = []
        for post in status:
            if 'likes' in post and 'comments' in post:
                val = {'updated_time': post['updated_time'], 'post_id':post['id'],
					   'likes':post['likes'], 'comments':post['comments']}
            elif 'likes' in post:
                val = {'updated_time': post['updated_time'], 'post_id':post['id'], 'likes':post['likes']}
            friend_status_info_dict = add_val_dictlist(author_id, val, friend_status_info_dict)
        current_person_status += 1
    return friend_status_info_dict

#heterosexual_post format is following:
#{author_id:[{'id':'post_id(1)', 'updated_time':time, 'like_ids':[heterosexual_ids], 'commen_ids':[heterosexual_ids]}, 
#            {'id':'post_id(2)', 'updated_time':time, 'like_ids':[heterosexual_ids], 'commen_ids':[heterosexual_ids]},
#             .....]}
#heterosexual_post is to remose some redudant attribute in posts
def heterosexual_post(posts, id_gender_dict, graph):
    print "mining post in statuses....."
    total_person_post = len(posts)
    current_person_post = 1
    heterosexual_post = dict()
    for key in posts.keys():
        print "person %d/%d" %(current_person_post, total_person_post)
        author_id = key
        author_gender = id_gender_dict[author_id]
        opp_gender = get_heterosexual(author_gender)
        total_post = len(posts[author_id])
        current_post = 1
        for post_msg in posts[author_id]:
            print "%d/%d....." %(current_post, total_post)
            heterosexual_likeslist = []
            heterosexual_comment_time_list = []
            post_id = post_msg['post_id']
            post_time = post_msg['updated_time']
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
                    obj_created_time = obj['created_time']
                    obj_profile = graph.get_object(obj_id)
                    if 'gender' in obj_profile and obj_profile['gender'] == opp_gender:
						heterosexual_comment_time_list.append({'comment_id':obj_id, 'comment_time':obj_created_time})

            val = {'author_gender':author_gender, 'post_id':post_id, 'updated_time':post_time,
				  'like_ids':heterosexual_likeslist,'comment_datas':heterosexual_comment_time_list }
            add_val_dictlist(author_id, val, heterosexual_post)

            print 'like size %d, ids %s' %(len(heterosexual_post[author_id][current_post-1]['like_ids']),
                                               heterosexual_post[author_id][current_post-1]['like_ids'])
            print 'comment size %d, ids %s' %(len(heterosexual_post[author_id][current_post-1]['comment_datas']),
                                                  heterosexual_post[author_id][current_post-1]['comment_datas'])
            current_post += 1
            #print heterosexual_post
            #if(current_post == 5):
            #    break
        filename = str(current_person_post) + '.csv'
        wrt_heterosexual_info(author_id, author_gender,
                              calulate_like_comment(heterosexual_post, 1),
                              filename)
        current_person_post += 1
        print "author_id: %s total_post %s" %(author_id, len(posts[key]))
    return heterosexual_post


