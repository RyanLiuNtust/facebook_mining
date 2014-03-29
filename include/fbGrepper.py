import facebook
import sys

def get_my_friends(graph):
    print "get friends...."
    friendlist = graph.get_connections('me','friends')['data']
    friends = [(friend['id'], friend['name'],) for friend in friendlist]
    print 'total of friend = %d\n' %len(friends)
    return friends

def get_my_feed(graph):
    print "get my feed...."
    feed_dict = graph.get_connections('me', 'feed')
    return feed_dict

def cvtDict2Chinese(dict):
    return str(dict).decode('unicode-escape')

#create a list of dict to save multiple dict with same key
def get_my_friends_about(graph, friends):
    print "get my friend about...."
    friendlist_about = []
    total_friend = len(friends)
    current_processing = 1
    for friend in friends:
        print "%d/%d....." %(current_processing,total_friend)
        friendlist_about.append(graph.get_object(friend[0]))
        current_processing += 1
    return friendlist_about
