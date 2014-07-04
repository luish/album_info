from utils import *


BASE_URL = 'http://coverartarchive.org/'


class CoverArtArchive:
    
    def get_release_cover(self, release_id):

    	url = BASE_URL + 'release/' + release_id

    	try:
    		json = get_json(url)
    		return json

    	except Exception, e:
    		pass

    	return None


## test

#cover_art = CoverArtArchive()
#print cover_art.get_release_cover('76df3287-6cda-33eb-8e9a-044b5e15ffdd')