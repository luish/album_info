from utils import *


class Vagalume:

    def __init__(self):
        self.base_url = 'http://www.vagalume.com.br/'


    def get_artist_info(self, name):
        
        url = self.base_url + name + '/index.js'
        json = get_json(url)
        result = None

        if 'artist' in json:
            artist = json['artist']
            albums = artist['albums']['item']

            if 'genre' in artist:
                genres = artist['genre']
            else:
                genres = None

            result = {
                'name': artist['desc'],
                'images': {
                    'medium': self.base_url + artist['pic_medium'], 
                    'small' : self.base_url + artist['pic_small']
                },
                'vagalume_url': self.base_url + artist['url'],
                'albums': albums,
                'genres': genres
            }

        return result