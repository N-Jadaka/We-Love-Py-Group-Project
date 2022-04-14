# The Movie Database
import requests

# Docs: https://www.themoviedb.org/documentation/api/discover

api_key = "3a5a85c5cb7b7dffd658882a47dde5d9"

movie_id = 343611
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}?"
endpoint = f"{api_base_url}{endpoint_path}api_key={api_key}"
r = requests.get(endpoint)
# Test Output
# print(endpoint)
# print(r.status_code)
# print(r.text)

# Taste Dive API
# Docs: https://tastedive-api-documentation.readthedocs.io/en/latest/index.html
# Similar Movie Comparisons
TD_API_KEY = '435478-MovieNig-HHTMI5RI'
new_movie = str(input('Please enter movie name '))
get_movies_endpoint = f'https://tastedive.com/api/similar?info=1&limit=1&q={new_movie}'
movie_data = requests.get(get_movies_endpoint)
# Test Output
print(movie_data.text)


# ImDB-API
IMDB_API_KEY = 'pk_brvs1xojoa0lnkpvq'
# Docs: https://imdb-api.com
get_top250_movies = f'https://imdb-api.com/en/API/Top250Movies/k_8uz05n2h'
top_data = requests.get(get_top250_movies)
# Test Output
print(top_data.text)
