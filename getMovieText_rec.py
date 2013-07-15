from __future__ import print_function
import sys
import json
from DBConnect import *
# =============================
# Do not modify above this line
def extractTweet(List):
  DEFAULT='manishranjna84'
  PATH="/home/manish/datasci_course_materials/projectMovie/logs/"
  FILE = PATH+List[0]+"_rec_pre.txt"
  FIN_FILE = PATH+"result/"+List[0]+"_rec.txt"
  inputdata = open(FILE)
  for line in inputdata:
    resultDict = json.loads(line)
    var = resultDict["statuses"]
    log = open(FIN_FILE, "w") 
    for i in range(20):
    	try: 
    		if 'text' in var[i]:
        		if ((var[i]['lang'])=='en'):
          			nameUser=var[i]['user']
                        	nameTwitter = nameUser['name']
          			if len(nameTwitter) == 0:
	    				nameTwitter = DEFAULT
	 			text = var[i]['text'].replace('\n','')
          			comb_text = nameTwitter + "#$#" +text.rstrip("\n")
          			print (comb_text.encode("utf-8"),file=log)
	except IndexError:
		pass 
	except ValueError:
		pass
# Do not modify below this line
# =============================
if __name__ == '__main__':
	counter=len(List)
	i = 0
        while ( counter > 0 ):
		extractTweet(List[i])
		i = i + 1
                counter = counter - 1
