import os
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie,TV
load_dotenv("KEYS.env")
api = os.getenv('API')

tmdb = TMDb()
tmdb.api_key = api
tv = TV()
movie = Movie() 
PosterPath = "https://image.tmdb.org/t/p/w600_and_h900_face"
s = None
def MovieTitle(movie_name):
    global s
    s = movie_name

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

def PopularMovie():
    popular = movie.popular()
    
    for p in popular:
        title = p.title
        desc = p.overview
        poster =PosterPath+ p.poster_path
        break
    return title, desc, poster
        