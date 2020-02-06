# The cursor object can be defined as an abstraction specified in the Python DB-API 2.0. It facilitates us to have multiple separate working environments through the same connection to the database. We can create the cursor object by calling the 'cursor' function of the connection object. The cursor object is an important aspect of executing queries to the databases.


import mysql.connector
myconn = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
cur = myconn.cursor()

print(cur)

