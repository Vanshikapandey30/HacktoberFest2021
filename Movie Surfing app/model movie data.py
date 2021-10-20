import imdb
import mysql.connector
import requests
import json
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MongoDB_2",
    database="movie"
)


mycursor = mydb.cursor()
sql="SELECT NAME FROM MOVIE_ID"
mycursor.execute(sql)
result=mycursor.fetchall()

num=2
mycursor = mydb.cursor()
query = "SELECT PLATFORM FROM MOVIE_ID WHERE ID=%s"
val = (num,)
mycursor.execute(query,val)
result=mycursor.fetchall()
print(result[0][0])
"""


a=0
dir=[]
for j in NAME:
    try:
        movies=ab.search_movie(j)
        index=movies[0].getID()
        movie=ab.get_movie(index)
        director = movie['director'][0]
        print(movie,director)
    except:
        continue
    #query = "UPDATE MOVIE_ID SET DIRECTOR = %s WHERE NAME = %s"
    #val = (director,j)
    #mycursor.execute(query,val)
    #mydb.commit()
    #a+=1
    #print(str(a)+" done")

for j in ID:
    api_request = requests.get("https://api.themoviedb.org/3/movie/"+str(j)+"?api_key=1d1059419394733b62f2b378982c8522&language=en-US")
    api = json.loads(api_request.content)
    genre = api['genres'][0]['name']
    
    query = "UPDATE MOVIE_ID SET GENRE = %s WHERE ID = %s"
    val = (genre,j)
    mycursor.execute(query,val)
    mydb.commit()
    print(str(j)+" done")
"""
