import urllib.request
import datetime
import threading
from time import ctime, sleep
# -*- coding: utf-8 -*-

def t1(func):
    for i in range(100):
        starttime = datetime.datetime.now()
        url = "http://127.0.0.1:9600/newsTitle?type="+urllib.parse.quote("网游")
        f = urllib.request.urlopen(url)
        s = f.read().decode('utf-8')
        endtime = datetime.datetime.now()
        print("round:%s, tread number:%s, returnValue:%s,\ntime:%f" % (i, func, s, (endtime - starttime).microseconds / 1000))
        sleep(1)


if __name__ == '__main__':
    threads = []
    for i in range(100):
        name = "t%s" % (i)
        name = threading.Thread(target=t1, args=(i,))
        threads.append(name)

    for t in threads:
        t.setDaemon(True)
        t.start()
