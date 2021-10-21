

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MongoDB_2",
    database="movie_python_db"
)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE cinema")

for x in mycursor:
    print(x)
