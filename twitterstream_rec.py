from __future__ import print_function
import oauth2 as oauth
import urllib2 as urllib
import sys
import datetime
from DBConnect import *

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "96058036-eaNafL62OwK9Af9rDYEZRScseYWLyDpu4YV05aCwq"
access_token_secret = "bhGsk0ELwfpFYJ99P5j0FXjOh1e8E3XOghfck0D2i8"

consumer_key = "lCHBtJ2By4CfZkz77A0g"
consumer_secret = "Ftdo6WuHeKJ5H86LEN4206dL3FommE2JmWWzZ6Nkc"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(https_handler)
  opener.add_handler(http_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples(List):
  log = open("/home/manish/datasci_course_materials/projectMovie/logs/"+List[0]+"_rec_pre.txt", "w")
  #url = "https://stream.twitter.com/1/statuses/filter.json?locations=-170.0,18.0,-60.0,72.0"
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d")
  #url  = "http://search.twitter.com/search.json?q=#YPD2 &rpp=10&page=10&result_type=recent&since=2013-06-07&until="+today
        #http://search.twitter.com/search.json?q=YPD2 &rpp=100&page=10&result_type=recent&since=2013-06-07&until=2013-06-10
  url = "https://api.twitter.com/1.1/search/tweets.json?q="+List[0]+" OR #"+List[2]+"&rpp=5&page=10&since="+List[1]+"&until="+today+"&result_type=recent&include_entities=true"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print (line.strip() , file= log) 

if __name__ == '__main__':
        counter=len(List)
	i = 0 
	while ( counter > 0 ):
		fetchsamples(List[i])
		i = i + 1
		counter = counter - 1
	








