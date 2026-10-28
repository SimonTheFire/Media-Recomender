import os
from pathlib import Path
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie,TV
KEY = Path(__file__).resolve().parent / "KEYS.env"

load_dotenv(KEY)
api = os.getenv('API')
tmdb = TMDb()
tv = TV()
movie = Movie() 

tmdb.api_key = api
PosterPath = "https://image.tmdb.org/t/p/w600_and_h900_face"
s = None
def MovieTitle(movie_name):
    global s
    s = movie_name

def ShowTitle(show_name):
    global s
    s = show_name

def RecomendMovie():
    film = movie.search(s)
    rec = film
    for res in rec:
        id = int(res.id)
        break
 
    rec = movie.recommendations(movie_id=id)
    for recommendation in rec:
        title = recommendation.title
        desc = recommendation.overview
        poster = PosterPath+recommendation.poster_path
        break 
    return title, desc, poster

def RecomendShow():
    show = tv.search(s)
    rec = show
    for res in rec:
        id = int(res.id)
        break
    rec = tv.recommendations(tv_id=id)
    for recommendation in rec:
        title = recommendation.name
        desc = recommendation.overview
        poster = PosterPath+recommendation.poster_path
        break 
    return title,desc,poster

def PopularMovie():
    popular = movie.popular()
    
    for p in popular:
        title = p.title
        desc = p.overview
        poster =PosterPath+ p.poster_path
        break
    return title, desc, poster

def PopularShow():
    popular = tv.popular()
    
    for p in popular:
        title = p.name
        desc = p.overview
        poster =PosterPath+ p.poster_path
        break
    return title, desc, poster