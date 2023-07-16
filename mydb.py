import mysql.connector

# Establish a connection to the MySQL server
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)

# Create a cursor object to execute SQL queries
cursorObject = dataBase.cursor()

# Create the 'elderco' database
cursorObject.execute("CREATE DATABASE elderco")

# Close the cursor and the database connection
#cursorObject.close()
#dataBase.close()

print('All done!')
