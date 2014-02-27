# -*- coding: utf-8 -*-

from lib.musicbrainz import MusicBrainz
from lib.lastfm import LastFm
from lib.vagalume import Vagalume
from lib.coverartarchive import CoverArtArchive
from lib.echonest import EchoNest


class ArtistInfo:
    
    def __init__(self, *args, **kwargs):
        self.result = {}


    def search_artist(self, artist_name):
        return MusicBrainz.search_artist(artist_name)


    def get_info(self, mbid):
        self.result['musicbrainz'] = MusicBrainz.get_artist_by_mbid(mbid)
        self.result['lastfm'] = LastFm().get_artist_info(mbid=mbid)

        return self.result