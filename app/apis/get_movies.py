import json
import requests

api_key = "DogrG9N6zAL9bzYc0KUA0DS0tj1hSlJa"
api_url_base = "https://api.nytimes.com/svc/movies/v2"


def get_critic_pick():
 
    query_message = {'critics-pick': 'Y', 
            'offset': '20', 'query': 'big', 'opening-date': '1980-01-01;1990-01-01', 'order': 'by-publication-date', 'publication-date': '1970-01-01;1980-01-01', 'reviewer': }
    api_url = '{0}/reviews/search.json?{1}&api-key={2}'.format(api_url_base, query_message, api_key)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

critic_pick = get_critic_pick()

if critic_pick is not None:
    print("Here are the critics' picks")
    for movie in critic_pick['results']:
        for k, v in movie.items():
            print('{0}:{1}'.format(k, v))
else:
    print('[!] Request Failed')
