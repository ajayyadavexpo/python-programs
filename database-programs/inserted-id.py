import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pythondb")  
#creating the cursor object  
cur = myconn.cursor()  
      
sql = "insert into Employee(name, id, salary, dept_id) values (%s, %s, %s, %s)"  
      
val = ("Mike",1005,28000,202)  
      
try:  
    #inserting the values into the table  
    cur.execute(sql,val)  
  
    #commit the transaction   
    myconn.commit()  
      
    #getting rowid  
    print(cur.rowcount,"record inserted! id:",cur.lastrowid)  
  
except:  
    myconn.rollback()  
  
myconn.close()  