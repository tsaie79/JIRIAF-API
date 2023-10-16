import mysql.connector

# establish a connection to the database with port 37082
## ssh -NfL 12345:localhost:37082 jiriaf2301
cnx = mysql.connector.connect(user='jiriaf', password='dikala-twiga', host='127.0.0.1', port='12345', database='jiriaf')

# create a cursor object
cursor = cnx.cursor()

# execute the query print out the tables in the database jiriaf

cursor.execute("SHOW TABLES")
for (table_name,) in cursor:
    print(table_name)

# close the cursor object
cursor.close()

# close the connection
cnx.close()