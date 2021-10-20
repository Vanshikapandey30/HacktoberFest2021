

from tkinter import *
from PIL import ImageTk,Image
import requests
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MongoDB_2",
    database="movie"
)


mycursor = mydb.cursor()
for i in range(2,2000):
    api_request = requests.get("https://api.themoviedb.org/3/movie/" +str(i)+ "?api_key=1d1059419394733b62f2b378982c8522&language=en-US")
    api = json.loads(api_request.content)
    
    if "id" in api:
        ID = api["id"]
        NAME = api["original_title"]
        VOTES = api["vote_count"]
        sql = "INSERT INTO movie_id (ID,NAME,votes) VALUES (%s,%s,%s)"
        val = (ID,NAME,VOTES)
        mycursor.execute(sql,val)
        mydb.commit()
        print(str(i)+ " done.")
    else:
        continue











"""
api_request = requests.get("https://api.themoviedb.org/3/trending/movie/week?api_key=1d1059419394733b62f2b378982c8522")
#api_request = requests.get("https://api.themoviedb.org/3/movie/497582?api_key=1d1059419394733b62f2b378982c8522&language=en-US")
api = json.loads(api_request.content)
#print(api)

trendinglist=[]
for i in range(10):
    TID = api['results'][i]['id']
    TNAME = api['results'][i]['title']
    li=[TNAME]
    trendinglist.append(li)
print(trendinglist)

#{'adult': False, 'backdrop_path': '/dFYguAfeVt19qAbzJ5mArn7DEJw.jpg', 'belongs_to_collection': {'id': 137697, 'name': 'Finding Nemo Collection', 'poster_path': '/xwggrEugjcJDuabIWvK2CpmK91z.jpg', 'backdrop_path': '/2hC8HHRUvwRljYKIcQDMyMbLlxz.jpg'}, 'budget': 94000000, 'genres': [{'id': 16, 'name': 'Animation'}, {'id': 10751, 'name': 'Family'}], 'homepage': 'http://movies.disney.com/finding-nemo', 'id': 12, 'imdb_id': 'tt0266543', 'original_language': 'en', 'original_title': 'Finding Nemo', 'overview': "Nemo, an adventurous young clownfish, is unexpectedly taken from his Great Barrier Reef home to a dentist's office aquarium. It's up to his worrisome father Marlin and a friendly but forgetful fish Dory to bring Nemo home -- meeting vegetarian sharks, surfer dude turtles, hypnotic jellyfish, hungry seagulls, and more along the way.", 'popularity': 43.888, 'poster_path': '/8h0CG12Oft1GqthLmsctg8iuQQj.jpg', 'production_companies': [{'id': 3, 'logo_path': '/1TjvGVDMYsj6JBxOAkUHpPEwLf7.png', 'name': 'Pixar', 'origin_country': 'US'}], 'production_countries': [{'iso_3166_1': 'US', 'name': 'United States of America'}], 'release_date': '2003-05-30', 'revenue': 940335536, 'runtime': 100, 'spoken_languages': [{'iso_639_1': 'en', 'name': 'English'}], 'status': 'Released', 'tagline': "There are 3.7 trillion fish in the ocean. They're looking for one.", 'title': 'Finding Nemo', 'video': False, 'vote_average': 7.8, 'vote_count': 13976}
#{'adult': False, 'belongs_to_collection': None,'genres': [{'id': 18, 'name': 'Drama'}], 'id': 550, 'original_language': 'en', 'original_title': 'Fight Club', 'overview': 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.', 'popularity': 42.241, 'poster_path': '/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 'production_companies': [{'id': 508, 'logo_path': '/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png', 'name': 'Regency Enterprises', 'origin_country': 'US'}, {'id': 711, 'logo_path': '/tEiIH5QesdheJmDAqQwvtN60727.png', 'name': 'Fox 2000 Pictures', 'origin_country': 'US'}, {'id': 20555, 'logo_path': '/hD8yEGUBlHOcfHYbujp71vD8gZp.png', 'name': 'Taurus Film', 'origin_country': 'DE'}, {'id': 54051, 'logo_path': None, 'name': 'Atman Entertainment', 'origin_country': ''}, {'id': 54052, 'logo_path': None, 'name': 'Knickerbocker Films', 'origin_country': 'US'}, {'id': 25, 'logo_path': '/qZCc1lty5FzX30aOCVRBLzaVmcp.png', 'name': '20th Century Fox', 'origin_country': 'US'}, {'id': 4700, 'logo_path': '/A32wmjrs9Psf4zw0uaixF0GXfxq.png', 'name': 'The Linson Company', 'origin_country': ''}], 'production_countries': [{'iso_3166_1': 'DE', 'name': 'Germany'}, {'iso_3166_1': 'US', 'name': 'United States of America'}], 'release_date': '1999-10-15', 'revenue': 100853753, 'runtime': 139, 'spoken_languages': [{'iso_639_1': 'en', 'name': 'English'}], 'status': 'Released', 'tagline': 'Mischief. Mayhem. Soap.', 'title': 'Fight Club', 'video': False, 'vote_average': 8.4, 'vote_count': 20096}
"""
