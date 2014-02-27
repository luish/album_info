from utils import *

class LastFm:
    
    def __init__(self, *args, **kwargs):
        pass


    def make_url(self, method, params = []):
        LASTFM_BASE_URL = 'http://ws.audioscrobbler.com/2.0/?format=json&api_key=f903ea5462ee374f0441bb4620af87d9'
        url = LASTFM_BASE_URL + '&method=' + method
        for param in params:
            url += '&' + param + '=' + urllib.quote_plus(str(params[param]))

        return url


    def get_top_artists_from_country(self, country):
        json = get_json(self.make_url('geo.gettopartists', {'limit': 10, 'country': country}))


    def get_artist_top_albums(self, artist_name):
        json = get_json(self.make_url('artist.gettopalbums', {'artist': artist_name, 'limit': 5}))


    def get_artist_info(self, name=None, mbid=None):
        
        if name:
            params = {'artist': name.encode('utf-8')}
        elif mbid:
            params = {'mbid': mbid.encode('utf-8')}
        else:
            return

        json = get_json(self.make_url('artist.getinfo', params))

        result = {
            'image': None,
            'lastfm_url': None,
            'mbid': None,
            'name': None,
            'summary': None,
            'year': None,
        }

        if 'artist' in json:
            artist = json['artist']

            result['name'] = artist['name']

            if 'mbid' in artist:
                result['mbid'] = artist['mbid']

            if 'url' in artist:
                result['lastfm_url'] = artist['url']

            if 'bio' in artist:
                if 'summary' in artist['bio']:
                    result['summary'] = artist['bio']['summary']

                if 'yearformed' in artist['bio']:
                    result['year'] = int(artist['bio']['yearformed'])
                elif 'formationlist' in artist['bio']:
                    if 'formation' in artist['bio']['formationlist']:
                        result['year'] = int(artist['bio']['formationlist']['formation']['yearfrom'])

            if 'image' in artist:
                last_img = len(artist['image']) - 1
                if last_img >= 0:
                    result['image'] = artist['image'][last_img]['#text']

        return result


    def get_artist_albums(self, name=None, mbid=None):

        if name:
            params = {'artist': name.encode('utf-8')}
        elif mbid:
            params = {'mbid': mbid.encode('utf-8')}
        else:
            return

        json = get_json(self.make_url('artist.gettopalbums', params))
        results = []

        for topalbums in json['topalbums']:
            albums = json['topalbums'][topalbums]

            for album in albums:
                if 'mbid' in album:
                    results.append(self.get_album_info(mbid=album['mbid']))

        return results


    def get_album_info(self, artist=None, album=None, mbid=None):

        if artist and album:
            params = {'artist': artist_name.encode('utf-8'), 'album': album_name.encode('utf-8')}
        elif mbid:
            params = {'mbid': mbid}
        else:
            return

        json = get_json(self.make_url('album.getinfo', params))

        result = {
            'artist': None,
            'date': None,
            'image': None,
            'lastfm_url': None,
            'mbid': None,
            'name': None,
            'summary': None,
            'tracks': [],
        }

        if 'album' in json:
            album = json['album']

            result['name'] = album['name']
            result['artist'] = album['artist']
            result['lastfm_url'] = album['url']

            if 'releasedate' in album:
                result['date'] = album['releasedate'].strip()

            if 'wiki' in album:
                if 'summary' in album['wiki']:
                    result['summary'] = album['wiki']['summary']

            if 'image' in album:
                last_img = len(album['image']) - 1 # index of the bigger image
                if last_img >= 0:
                    result['image'] = album['image'][last_img]['#text']
                
            if 'mbid' in album:
                result['mbid'] = album['mbid']

            if 'tracks' in album:
                tracks = album['tracks']

                try:
                    for track in tracks:
                        if track == u'track':
                            t = tracks[track]
                            i = 1
                            for attr in t:
                                result['tracks'].append( {
                                    'track': i,
                                    'name': attr['name'],
                                    'duration': attr['duration'],
                                    'lastfm_url': attr['url'],
                                    'mbid': attr['mbid']
                                } )
                                i += 1

                except TypeError, e:
                    #print e
                    pass

        return result
