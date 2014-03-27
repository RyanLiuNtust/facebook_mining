import facebook
import sys

auth_access_token = "CAACEdEose0cBAGorutD9JZCp6lkCz8p10DdgJXbJ6Nb5x0AOXUN8FJLCwzXR6ZAMZCDpuZBfWZBSPPbr5ecp2ReQM27FYp80a2ciOExxqOkY0okaHH0gbrmlxYWblKlZBVZCfCjdXRookx5ZC1BM041ue9JsMV6x5RBGNDONJxUfb8MTzj4p4WsSCmvZClECMPpfW8MhOT3ZA4XQZDZD"

def getMyFriends(graph):
    print "get friends....\n"
    friendlist = graph.get_connections('me','friends')['data']
    friends = [(friend['id'], friend['name'],) for friend in friendlist]
    print 'total of friend = %d\n' %len(friends)
    return friends

def getMyFeed(graph):
    print "get my feed....\n"
    feed_dict = graph.get_connections('me', 'feed')
    return feed_dict

def cvtDict2Chinese(dict):
    return str(dict).decode('unicode-escape')

def main():
    graph = facebook.GraphAPI(auth_access_token)
    friends = getMyFriends(graph)
    feed = getMyFeed(graph)
    print cvtDict2Chinese(feed)

if __name__ == "__main__":
    main()

