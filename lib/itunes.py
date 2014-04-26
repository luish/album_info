from utils import *

ITUNES_KEY = ''
BASE_URL = 'https://itunes.apple.com/'

class iTunes:

    def __init__(self):
        pass


    def search_song(self, term):
        url = BASE_URL + 'search?term=' + term + '&entity=musicTrack&limit=1'
        json = get_json(url)
        result = None

        if json and 'results' in json and json['resultCount'] > 0:
            result = json['results'][0]

        return result


    def lookup(self, id):
        url = BASE_URL + 'lookup?id=' + id
        json = get_json(url)
        result = None

        if json and 'results' in json and json['resultCount'] == 1:
            result = json['results'][0]

        return result


# example
#i = iTunes()
#print i.search_song('skank - sutilmente')
#print i.lookup('157890919')