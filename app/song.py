import requests


def getSong(key):
    return requests.get('http://ws.audioscrobbler.com/2.0/',
                        headers={'user-agent': 'kingeinhorn'},
                        params={'api_key': key, 'method': 'user.getrecenttracks', 'format': 'json',
                                'user': 'kingeinhorn'})
