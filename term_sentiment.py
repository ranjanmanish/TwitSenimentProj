
import urllib
import json
import sys

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

tweetFile = open (sys.argv[1])
for line in tweetFile:
  sentiment = 0
  resultdict = json.loads(line)
  if 'text' in resultdict :
    Text=resultdict.get('text')
    thisLine = Text.split(" ")
    for word in thisLine:
      if word in scores:
        sentiment = sentiment + scores[word] 
    for word in thisLine:
      if word in scores:
        temp = scores[word]
	try:
          print word+" "+str(temp) 
	except ValueError:
	  print 0
      else:
        try:
          print word+" "+str(sentiment)
        except ValueError:
	  print 0
