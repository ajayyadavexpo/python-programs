import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pythondb")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #updating the name of the employee whose id is 110  
    cur.execute("update Employee set name = 'John' where id = 110")  
    myconn.commit()  
except:  
      
    myconn.rollback()  
  
myconn.close()  