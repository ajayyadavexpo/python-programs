import mysql.connector

myconn = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")

cur = myconn.cursor()

try:
	cur.execute("select * from employee")

	result = cur.fetchall()

	for row in result:
		print(row)
except:
	myconn.rollback()

myconn.close()