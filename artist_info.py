# -*- coding: utf-8 -*-

from lib.musicbrainz import MusicBrainz
from lib.lastfm import LastFm
from lib.vagalume import Vagalume
from lib.coverartarchive import CoverArtArchive
from lib.echonest import EchoNest
from lib.discogs import Discogs


class ArtistInfo:
    
    def __init__(self, *args, **kwargs):
        self.result = {}


    def search_artist(self, artist_name):
        return MusicBrainz.search_artist(artist_name)


    def get_info(self, mbid, name=None):
        self.result['musicbrainz'] = MusicBrainz.get_artist_info(mbid)
        self.result['lastfm'] = LastFm().get_artist_info(mbid=mbid)
        self.result['vagalume'] = Vagalume().get_artist_info(name)
        self.result['discogs'] = Discogs().get_artist_info(name)
        self.result['echonest'] = EchoNest().get_artist_info(name)
        #self.result['coverartarchive'] = CoverArtArchive().get_artist_images(mbid)

        return self.result