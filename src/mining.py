#version 1.0
#Author RyanLiuNtust
#Time 3/29
import facebook
import sys

auth_access_token = "CAACEdEose0cBANeU2xzzxZBx16HZCwYNnAhT85A8PBgcM9isKC86jFYp5UEddhkhCbgaV4cqUMKxFPvhI8KckQDYcxjZCc4zCRwAlmI4fnB1WGlXpVBYeEves5S0Pjs1aRxgtPZCvdmZCBovZByX0fOpPdsbvOpuF7R8sTdyEc9IcGZBqCjoNGD07dDstsOFUokiPsg3mOTywZDZD"

def get_my_friends(graph):
    print "get friends....\n"
    friendlist = graph.get_connections('me','friends')['data']
    friends = [(friend['id'], friend['name'],) for friend in friendlist]
    print 'total of friend = %d\n' %len(friends)
    return friends

def get_my_feed(graph):
    print "get my feed....\n"
    feed_dict = graph.get_connections('me', 'feed')
    return feed_dict

def cvtDict2Chinese(dict):
    return str(dict).decode('unicode-escape')

#create a list of dict to save multiple dict with same key
def get_my_friends_about(graph, friends):
    friendlist_about = []
    total_friend = len(friends)
    current_processing = 1
    for friend in friends:
        print "%d/%d....." %(current_processing,total_friend)
        friendlist_about.append(graph.get_object(friend[0]))
        current_processing += 1
    return friendlist_about

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = get_my_friends(graph)
    feed = get_my_feed(graph)
    print friends
    print cvtDict2Chinese(feed)
    friendlist_about = get_my_friends_about(graph, friends)
    for about in friendlist_about:
        if 'gender' in about:
            print about["name"] + " " + about["gender"]

if __name__ == "__main__":
    main()

