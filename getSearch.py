import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=Microsoft")
print json.load(response)
