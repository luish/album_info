import os
import pyen

try:
    ECHONEST_API_KEY = os.environ['ECHONEST_API_KEY']
except KeyError:
    print 'ECHONEST_API_KEY not found'
    quit(1)


class EchoNest:

    def __init__(self):
        self.echonest = pyen.Pyen(ECHONEST_API_KEY)


    def get_artist_info(self, name):
        response = self.echonest.get('artist/biographies', name=name)
        return response