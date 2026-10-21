import os
from dotenv import load_dotenv
from tmdbv3api import TMDb, Movie,TV
load_dotenv("KEYS.env")
api = os.getenv('API')

tmdb = TMDb()
tmdb.api_key = api
tv = TV()
movie = Movie() 
def SearchMovie():
    s = input()
    film = movie.search(s)
    rec = film.id
    rec = movie.recommendations(movie_id=rec)
    for recommendation in rec:
        print(recommendation.title+"\n")
        print(recommendation.overview+"\n")    

def SearchTV():
    s = input()
    show = tv.search(s)
    for result in show:
        print("")
        print(result.name+"\n")
        print(result.overview+"\n")

SearchMovie()
SearchTV()