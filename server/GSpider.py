import urllib.request
import re
import time
from mong import mongoapi
url = 'http://www.gamersky.com/news/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/62.0.3202.94 Safari/537.36',
    'Referer': url,
}

def ajax():
    now = str(int(time.time()));
    print(int(now));
    contents = [];
    END = 3;
    for i in range(1,END):
        page = str(i)
        url = 'http://db2.gamersky.com/LabelJsonpAjax.aspx?callback=jQuery18309820627977549694_'+now+'&jsondata={"type":"updatenodelabel","isCache":true,"cacheTime":60,"nodeId":"11007","isNodeId":"true","page"' ':'+page+'}'
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        contents.append(content)
        #print(contents)
        time.sleep(10);
    return contents
#为方便编写 网页解析代码也同样放在这里
def webPars(html):
    request = urllib.request.Request(html, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    bodyPattern  = re.compile('<div class="Mid2L_con">(.*?)<!--文章内容导航 结束-->',re.S);
    bodyl = re.findall(bodyPattern, content)
    #print(bodyl)
    mong = mongoapi(db='newsDetail');
    mong.showAll();
    body = "".join(bodyl)
    body = body.replace(u'\u3000',u'')
    print(html+"body"+body)
    bodPattern  = re.compile('<p.*?>(.*?)</p>',re.S)
    bod = re.findall(bodPattern,body)
    id = 0
    for item in bod:
        print("item"+item)
        item = item.replace('<br>','');
        if(item.find('src')>0):
            print("href"+item)
            item = item.replace('" border="0','')
            bodyImgPattern = re.compile('<a.*?src="(.*?)">',re.S)
            bodyImg = re.findall(bodyImgPattern,item);
            for imgItem in bodyImg:
                print(imgItem)
                if(imgItem != '//pub.idqqimg.com/wpa/images/group.png'):
                    imgspider(imgItem)
                urlpattern = re.compile('/.*?2018/(.*?).jpg', re.S)
                urlname = re.findall(urlpattern, imgItem)
                urlname = ''.join(urlname)
                urlname = urlname.replace('/','')
                if(len(urlname)>25):
                    urlname = urlname[-25:]
                if(urlname != ''):
                    urlname = 'http://127.0.0.1:9600/image/' + urlname
                    mong.insertDetail('image',urlname,id,html);
                    id = id + 1
        elif(item.find('span')>0):
            item = item.replace('<span style="font-weight: bold;">', '');
            item = item.replace('</span>','');
            item = item.replace('<span style="FONT-WEIGHT: bold">', '');
            print("span"+item);
            mong.insertDetail('p',item,id,html)
            id = id + 1
        elif(item.find('script')>0):
            pass
        elif(item.find('strong')>0):
            pass
        elif(item.find('更多资讯请关注')>0):
            pass
        else:
            print(item);
            mong.insertDetail('p',item,id,html)
            id = id +1
def imgspider(url):
    urlpattern = re.compile('2018/(.*?).jpg',re.S)
    urlname = re.findall(urlpattern,url)

    urlname = ''.join(urlname)
    urlname = urlname.replace('/', '')
    if (len(urlname) > 25):
        urlname = urlname[-25:]
    try:
        urllib.request.urlretrieve(url, r'C:\Users\xu\Documents\GitHub\News\server\image\%s.jpg' %urlname)
    except Exception as e:
        print(url+"图片无法下载")
def xkspider(url):
    contents = ajax()
    mong = mongoapi();
    for content in contents:
        content = content.replace("\\","")
        parttern = re.compile('<li>(.*?)</li>', re.S)
        items = re.findall(parttern,content)
        #print(items);
        for item in items:
            titPattern = re.compile('alt="(.*?)"', re.S);
            tit = re.findall(titPattern,item);
            title = "".join(tit);
            imgPattern = re.compile('<img src="(.*?)"',  re.S);
            image = re.findall(imgPattern, item)
            imgSrc = "".join(image)
            jumpPattern = re.compile('<a class="tt" href="(.*?)"', re.S);
            jumpA = re.findall(jumpPattern, item);
            jumpUrl = "".join(jumpA);
            relTiPattern = re.compile('class="time">(.*?)<',re.S);
            relTi = re.findall(relTiPattern, item);
            relTime = "".join(relTi);
            if(imgSrc):
                #print(item);
                #print("title:"+title+"imgSrc:"+imgSrc+" jumpUrl:"+jumpUrl+" time:"+relTime);

                urlpattern = re.compile('2018/(.*?).jpg', re.S)
                urlname = re.findall(urlpattern, imgSrc)
                urlname = ''.join(urlname)
                urlname = 'http://127.0.0.1:9600/image/'+urlname
                mong.insert(title,urlname,jumpUrl,relTime)
                webPars(jumpUrl);
                imgspider(imgSrc)
    mong.showAll()
xkspider(url)
#ajax();