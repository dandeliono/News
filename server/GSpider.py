import urllib.request
import re
import time
url = 'http://www.gamersky.com/news/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/62.0.3202.94 Safari/537.36',
    'Referer': url,
}

def ajax():
    now = str(int(time.time()));
    print(int(now))
    contents = []
    for i in range(1,10):
        print(type(i))
        page = str(i)
        print(type(page))
        url = 'http://db2.gamersky.com/LabelJsonpAjax.aspx?callback=jQuery18309820627977549694_'+now+'&jsondata={"type":"updatenodelabel","isCache":true,"cacheTime":60,"nodeId":"11007","isNodeId":"true","page"' ':'+page+'}'
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')

        print(content)
        contents.append(content)
        print(contents)
        time.sleep(10);
    return contents
def xkspider(url):
    contents = ajax()
    for content in contents:
        content = content.replace("\\","")
        parttern = re.compile('<li>(.*?)</li>', re.S)
        items = re.findall(parttern,content)
        print(items);
        for item in items:
            titPattern = re.compile('title="(.*?)"', re.S);
            tit = re.findall(titPattern,item);
            title = "".join(tit);
            imgPattern = re.compile('<img src="(.*?)"',  re.S);
            image = re.findall(imgPattern, item)
            imgSrc = "".join(image)
            if(imgSrc):
                #print(item);
                print("title:"+title+"imgSrc:"+imgSrc)
xkspider(url)
#ajax();