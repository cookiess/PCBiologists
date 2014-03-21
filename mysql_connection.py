#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "127.0.0.1", user = "temp", passwd = "temp", db = "test")
# prepare a cursor object using cursor() method
cursor = connection.cursor()
# execute the SQL query using execute() method.
SQL = "select name_first, name_last from address"
cursor.execute(SQL)
# fetch all of the rows from the query
#data = cursor.fetchall()
data = cursor.fetchone()
print data
# print the rows
for row in data :
	print row[0], row[1]
# close the cursor object
cursor.close()
# close the connection
connection.close()
# exit the program
sys.exit()