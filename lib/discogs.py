import discogs_client as discogs

discogs.user_agent = 'artist_info 0.1 http://github.com/luis/artist_info'


class Discogs:
    
    def __init__(self):
        pass


    def get_artist_info(self, artist_name):

        result = {}

        try:
            artist = discogs.Artist(artist_name)

            if (artist):
                result['name'] = artist.name
                result['data'] = artist.data
                result['aliases'] = map(lambda x: x.name, artist.aliases)
                #result['releases'] = artist.releases

        except discogs.DiscogsAPIError:
            pass

        return result
