import cProfile
import urllib.request


def proTest():
    url = "http://127.0.0.1:9600/newsTitle?type=" \
          + urllib.parse.quote("网游")
    f = urllib.request.urlopen(url)
    s = f.read().decode('utf-8')


if __name__ == '__main__':
    cProfile.run('proTest()')