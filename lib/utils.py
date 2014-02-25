import urllib
import json

def urlfetch(url):
    if url:
        u = urllib.urlopen(url)
        if u:
            return u.read()
    return None


def get_json(url):
    content = urlfetch(url)
    try:
        return json.loads(content)
    except ValueError, e:
        print 'Error: ', e