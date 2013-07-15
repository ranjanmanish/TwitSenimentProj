from __future__ import print_function
import sys
import json

# =============================
# Do not modify above this line
def extractTweet(inputdata):
  for line in inputdata:
    
    resultDict = json.loads(line)
    var = resultDict["results"]
    log = open("/home/manish/datasci_course_materials/projectMovie/"+List[0]+"_pop.txt", "w")
    for i in range(10):
      print (var[i]['from_user_name'].strip() +":"+var[i]['text'].strip(),file = log) 
      #print (line.strip() , file= log) 
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  extractTweet(inputdata)
