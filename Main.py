import os
from dotenv import load_dotenv
import tmdbsimple as tmdb

load_dotenv("KEYS.env")
api = os.getenv('API')
tmdb.API_KEY = api
tmdb.REQUESTS_TIMEOUT = 5

search = tmdb.Search()
response = search.movie(query='The Bourne')
for s in search.results:
    print(s['title'],s['release_date'])