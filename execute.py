import sys, pprint
from artist_info import ArtistInfo

def usage():
    return 'Usage: %s [artist name]' % sys.argv[0]


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print usage()
        quit(1)

    artist_info = ArtistInfo()
    pp = pprint.PrettyPrinter(depth=6)

    search = artist_info.search_artist(' '.join(sys.argv[1:]))

    i=1
    for r in search['artist-list']:
        if 'disambiguation' in r:
            print '%d\t - %s (%s)' % (i, r['name'], r['disambiguation'])
        else:
            print '%d\t - %s' % (i, r['name'])
        i += 1

    num = int(input('Selecione o numero do artista correto: '))
    if (len(search['artist-list']) > num-1):
        mbid = search['artist-list'][num-1]['id']

        info = artist_info.get_info(mbid)

        pp.pprint(info)

