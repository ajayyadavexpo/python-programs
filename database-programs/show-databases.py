import mysql.connector as con

myconnection = con.connect(host="localhost",user="root",passwd="")
cur = myconnection.cursor()

try:
	#Creating new databases
	cur.execute("create database newpython_db")
	dbs = cur.execute("show databases")
except:
	myconnection.rollback()

for x in cur:
	print(x)

myconnection.close()
