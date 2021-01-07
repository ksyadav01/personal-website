import requests

from app.constants import LAST_API_KEY


def getSong():
    return requests.get('http://ws.audioscrobbler.com/2.0/',
                        headers={'user-agent': 'kingeinhorn'},
                        params={'api_key': LAST_API_KEY, 'method': 'user.getrecenttracks', 'format': 'json',
                                'user': 'kingeinhorn'})

