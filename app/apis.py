import json
import requests

api_key = "DogrG9N6zAL9bzYc0KUA0DS0tj1hSlJa"
api_url_base = "https://api.nytimes.com/svc/movies/v2"


def get_movies(query):
    api_url = '{0}/reviews/search.json?'.format(api_url_base, api_key)
    query.update({'api-key': api_key})
    response = requests.get(api_url, params=query)
    if response.status_code == 200:
        movies = json.loads(response.content.decode('utf-8'))["results"]
        return [i["display_title"] for i in movies ]
    else:
        return None

