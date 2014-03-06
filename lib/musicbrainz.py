import musicbrainzngs

musicbrainzngs.set_useragent('artist_info', '0.1', 'http://github.com/luis/artist_info')


class MusicBrainz:
    
    def __init__(self):
        pass


    @staticmethod
    def search_artist(name):
        results = musicbrainzngs.search_artists(name)
        return results


    @staticmethod
    def get_artist(mbid):
        artist = musicbrainzngs.get_artist_by_id(mbid, ['releases'])
        return artist


    @staticmethod
    def get_artist_info(mbid):
        result = musicbrainzngs.get_artist_by_id(mbid, ['url-rels', 'tags'])
        releases = musicbrainzngs.browse_releases(artist=mbid, limit=100)

        result['artist']['release-list'] = releases['release-list']
        return result

    @staticmethod
    def get_release_by_id(mbid):
        release = musicbrainzngs.get_release_by_id(mbid, ['artists', 'recordings', 'labels', 'release-groups'])
        release = release['release']
        result = {
            'mbid': None,
            'artist': None,
            'name': None,
            'country': None,
            'date': None,
            'status': None,
            'tracks': [],
            'amazon': None,
            'year': None,
        }

        result['artist'] = release['artist-credit'][0]['artist']
        result['mbid'] = release['id']
        result['name'] = release['title']

        if 'date' in release:
            d = release['date'].split('-')
            if len(d) == 3:
                result['date'] = release['date']
            if len(d) >= 1:
                result['year'] = d[0]

        if 'country' in release:
            result['country'] = release['country']

        if 'status' in release:
            result['status'] = release['status']

        if 'asin' in release:
            result['amazon'] = release['asin']

        if len(release['medium-list']) > 0 and 'track-list' in release['medium-list'][0]:
            for track in release['medium-list'][0]['track-list']:
                result['tracks'].append(track)

        return result