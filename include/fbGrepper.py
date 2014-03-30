import facebook
import sys
def enum(**enums):
    return type('Enum', (), enums)

FRIEND_INFO = enum(ABOUT = 'about', STATUSES = 'statuses')

def get_my_friends(graph):
    print "get friends...."
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
    print "get my friend about...."
    friendlist_about = []
    total_friend = len(friends)
    current_friend = 1
    for friend in friends:
        print "%d/%d....." %(current_friend, total_friend)
        friendlist_about.append(graph.get_object(friend[0]))
        current_friend += 1
    return friendlist_about

#statuses is defined that you post on your own wall
#friendlist_status save as [id, status_list corresponding to id]
def get_my_friends_status(graph, friends):
    print "get my friends status...."
    friendlist_status = []
    total_friend = len(friends)
    current_friend = 1
    for friend in friends:
        print "%d/%d....." %(current_friend, total_friend)
        id = friend[0]
        friendlist_status.append((id, graph.get_connections(id, 'statuses')['data']))
        current_friend += 1
    return friendlist_status

def get_likes(friendlist_status):
    print "get likes info about statuses...."
    friendlist_like = []
    total_statuses = len(friendlist_status)
    current_status = 1
    for s in friendlist_status:
        print "%d/%d...." %(current_status, total_statuses)
        status = s[1]
        for post in status:
            if 'message' in post and 'likes' in post:
                #save nessage for testing,and consider whether the corresponding comment need to be saved
                friendlist_like.append((post['message'], post['likes']))
        current_status += 1
    return friendlist_like
