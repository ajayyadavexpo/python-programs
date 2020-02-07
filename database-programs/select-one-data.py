import mysql.connector

myconn = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")

cur = myconn.cursor()

try:
	cur.execute("select id,name from employee")

	result = cur.fetchone()
	print(result)
	
except:
	myconn.rollback()

myconn.close()