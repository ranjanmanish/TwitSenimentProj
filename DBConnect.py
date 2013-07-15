import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="cxps123", # your password
                      db="TestDB") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM MovieD")

# print all the first cell of all the rows
List = []
List = cur.fetchall()
#print List[0][0]   # this is list of list in case th query returns more than one value
#for row in cur.fetchall() :
#  List.append[row]  
