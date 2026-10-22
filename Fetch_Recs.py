import os
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie,TV
load_dotenv("KEYS.env")
api = os.getenv('API')

tmdb = TMDb()
tmdb.api_key = api
tv = TV()
movie = Movie() 

s = None
def MovieTitle(movie_name):
    global s
    s = movie_name

def RecomendMovie(s):
    film = movie.search(s)
    rec = film
    
    for res in rec:
        rec = res.id
        break
    
    rec = movie.recommendations(movie_id=rec)
    for recommendation in rec:
        title = recommendation.title
        desc = recommendation.overview
        break 
    return title, desc

def SearchTV():
    s = input()
    show = tv.search(s)
    for result in show:
        print("")
        print(result.name+"\n")
        print(result.overview+"\n")
