from __future__ import print_function
import sys
import json
from DBConnect import *
# =============================
# Do not modify above this line
def extractTweet(List):
  DEFAULT='manishranjan84'
  PATH="/home/manish/datasci_course_materials/projectMovie/logs/"
  FILE = PATH+List[0]+"_pop_pre.txt"
  FIN_FILE = PATH+List[0]+"_pop.txt"
  inputdata = open(FILE)
  for line in inputdata:
    resultDict = json.loads(line)
    var = resultDict["statuses"]
    log = open(FIN_FILE, "w") 
    for i in range(15): 
    	if 'text' in var[i]:
        	if ((var[i]['lang'])=='en'):
          		nameUser=var[i]['user']
                        nameTwitter = nameUser['name']
          		if len(nameTwitter) == 0:
	    			nameTwitter = DEFAULT
	 		text = var[i]['text'].replace('\n','')
          		comb_text = nameTwitter + "#$#" +text.rstrip("\n")
          		print (comb_text.encode("utf-8"),file=log) 
      #print (line.strip() , file= log) 
# Do not modify below this line
# =============================
if __name__ == '__main__':
        counter=len(List)
        while ( counter > 0 ):
                extractTweet(List[0])
                counter = counter - 1

