import facebook
import numpy

def getFriends(graph):
	print "get friends....\n";
	jsonFriends = graph.get_connections('me', 'friends')['data']
	friends = [(friend['id'], friend['name'],) for friend in jsonFriends]
	return friends

auth_access_token = "CAACEdEose0cBAM4ieZCok6FwFUpfPZBCEGoHP91jAeIkt1b8lDAwZCmq7kZBYCrFKzj7E4OuNt3yZAsl0LNyQyORBhZBoQZAnl9ZAcREsOqNtJuqOWNEpsHTzE6lveXTqIvht4SpoYo2wlcZC8PAMkw5up0xRqDS1S4f6E4iHMWetDu6m2ZCgMok4jyo4hHZBygbWkZD"

graph = facebook.GraphAPI(auth_access_token)
friends = getFriends(graph)
print friends
