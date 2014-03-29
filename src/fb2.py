import facebook
#import numpy

ACCESS_TOKEN='CAACEdEose0cBAOLEZAVPEp8kp1pZBPZAz7mtdG4q2PwrXX80UReBxkmJ0E0xoC5KMcnZAxjwg0lP9s0FlSyAHlZAX92Hr4tp9L60Q6TYUxQeLpLwpuovBgpr7ZBIZA02ZBqNH883Ph96UWZCsCYA4V5n1iW4ZAvdedOUpM1TnZAdClef0ykq1xDvoNG8lZBlmZAhiRKbhZBsoeR3hTwwZDZD'
fb=facebook.GraphAPI(ACCESS_TOKEN)


def getFriend(fb):
    print("Get Friends")
    jsonFriends = fb.get_connections('me','friends')['data']#My Friends-->Data 

    friends = [(friend['id'], friend['name']) for friend in jsonFriends]
    
    return friends

def getFriend_Friends(friends,fb):
    F_friends = {}
    
    for friend in friends:
        
        F_friends[friend[0]] = fb.get_connections(friend[0],'friends')['data']
        print friend[1]
        print F_friends[friend[0]]
        print ""
    return F_friends

#---------------------------------------------------------------------------------------
def main():
    test_friends = {}

    friends=getFriend(fb)   #friends[num][0]-->id , friends[num][1]-->name

    for i in range(0,len(friends),1):
        print friends[i][1]
        test=fb.get_object(friends[i][0])
        if 'gender' in test:
            print test['gender']
    
    
if __name__ == "__main__":
    main()
    
    
#test_friends=getMutualFriends(friends,fb)

#test_friends[2]
