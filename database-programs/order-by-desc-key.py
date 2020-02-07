import mysql.connector

myconn = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")

cur = myconn.cursor()

try:
	cur.execute("select name,id,salary from employee order by name desc")

	result = cur.fetchall()
	print("Name id Salary")

	for row in result:
		print("%s %d %d"%(row[0],row[1],row[2]))
	
except:
	myconn.rollback()

myconn.close()