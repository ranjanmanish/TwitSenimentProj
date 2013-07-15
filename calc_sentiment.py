
import urllib
import json
import sys
import re

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

tweetFile = open (sys.argv[1])
MovieName = "ankur arora murder case"
for line in tweetFile:
	sentiment = 0
	try:
		#print "Line is",line
		this=line.split("#$#")
        	wordArray=this[1].split(" ")
		for word in wordArray:
	  		word=re.sub('\W', '', word)
			word = word.lower()
			if word in scores:
				if word in MovieName:
					sentiment = sentiment + 0
				else:
					sentiment = sentiment + scores[word]
		print this[0]+":"+this[1]+":"+str(sentiment) 		
	except ValueError:
		pass
