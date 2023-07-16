 
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin'   
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco")

print('All done !')