import tornado.web
import tornado.ioloop

from artist_info import ArtistInfo


class ArtistSearchHandler(tornado.web.RequestHandler):

    def get(self, artist_name):
        response = ArtistInfo().search_artist(artist_name)
        self.write(response)


class ArtistInfoByMbidHandler(tornado.web.RequestHandler):

    def get(self, mbid, name):
        response = ArtistInfo().get_info(mbid, name)
        self.write(response)


app = tornado.web.Application([
    (r'/search/([a-z0-9 -]+)', ArtistSearchHandler),
    (r'/info/(.*)/(.*)?', ArtistInfoByMbidHandler),
])

if __name__ == '__main__':
    print 'Listening on http://127.0.0.1:8888'
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()