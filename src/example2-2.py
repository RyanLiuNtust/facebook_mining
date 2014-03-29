import facebook # pip install facebook-sdk
import json
# A helper function to pretty-print Python objects as JSON
def pp(o):
    print json.dumps(o, indent=1)
# Create a connection to the Graph API with your access token
ACCESS_TOKEN = 'CAACEdEose0cBAG570mZBQGdOXoTQY4z9HwDO87KnFDXowc2dAxnoc0vZC8QzZChsRZAOYPE9SjLsY4UwJVz5MPTLhmmZBzircFZA86bF0EDJVBuT9u2lTCqNsem0YRPx43rfLBss2d0ORZC2ZCDD83OLKGZBmiZBZA4Wc0cwCMpWHECZBgP86wywZCTvZARrM5QrIkn0lfSlOcO8yqWgZDZD'
g = facebook.GraphAPI(ACCESS_TOKEN)
# Execute a few sample queries
print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))
print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me', 'friends'))
print
print '---------------'
print 'Social Web'
print '---------------'
pp(g.request("search", {'q' : 'social web', 'type' : 'page'}))
print
print '---------------'
print 'Query for Mining the Social Web'
print '---------------'
mtsw_id = '146803958708175'
pp(g.get_object(mtsw_id))
pp(g.get_object('http://shop.oreilly.com/product/0636920030195.do'))
