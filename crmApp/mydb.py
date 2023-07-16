import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create the database
cursorObject.execute("CREATE DATABASE elderco")
print("All is done!")