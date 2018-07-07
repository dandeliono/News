import urllib.request

from flask import Flask, Response
from flask import request

from unit.mong import *

# -*- coding: utf-8 -*-
mongo = newsItem
#mongo = mongoapi();
mongoDetail = newsDetail()
#mongoDetail = mongoapi(db='newsDetail')
#mongoHistory = mongoapi(db='History')
mongoHistory = History()
#mongoComment = mongoapi(db='comment')
mongoComment = Comment()
app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

@app.route('/newsTitle', methods=['GET', 'POST'])
def newsTitle():
    searchword = request.args.get('type', '')
    openid = request.args.get('openid','')
    print("serachword"+searchword);
    newsList=[]
    if(openid):
        newsList = list(mongo.getNewsByOpenid(openid))
        print(newsList)
    if request.method == 'GET':
        newsList = newsList+mongo.selectByTy(searchword)
    print(newsList)
    newsTitle = {
        "code": 200,
        "message":"success",
        "result":newsList
    }
    return json.dumps(newsTitle);
@app.route('/newsDetail',methods=['GET','POST'])
def newsDetail():
    openid = request.args.get('openid','')
    searchword = request.args.get('hash', '')
    newsList = mongoDetail.selectByHash(searchword)
    title = mongo.selectTitle(searchword)
    date = mongo.selectDate(searchword)

    readerCount = int(mongo.selectReaderCount(title))+1
    times = time.strftime("%Y-%m-%d %H:%M:%S")
    mongoHistory.insertHistory(openid, title,times)
    firstImage = mongo.selectFirstImg(searchword)

    result ={
        "id":searchword,
        "title":title,
        "date":date,
        "source":"",
        "firstImage": firstImage,
        "content":newsList,
        'readCount':readerCount
    }
    newsDetail={
        "code":200,
        "message":"success",
        "result":result
    }
    print(newsDetail)
    return json.dumps(newsDetail)
@app.route('/comment',methods=['POST'])
def comment():
    comment = request.form.get('comment')
    openid = request.form.get('openid')
    title = request.form.get('title')
    mongoComment.inserctCommetn(openid,comment,title)
    return ''
@app.route('/onLogin')
def onlogin():
    code = request.args.get('code', '')
    print(code)
    openid = getOpenid(code)
    return openid
def getOpenid(code):
    APPID = 'wxa810679bf9074888'
    SECRET = '94eb0016d4a3a55d638d3abd31066562'
    url='https://api.weixin.qq.com/sns/jscode2session?appid='+APPID+'&secret='+SECRET+'&js_code='+code+'&grant_type=authorization_code'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(json.loads(content)['openid'])
    return json.loads(content)['openid']
@app.route("/image/<imageid>")
def index(imageid):
    #print(imageid)
    if(imageid != ''):
        try:
            image = open("image/{}.jpg".format(imageid),mode='rb')
            #print(image)
        except Exception:
            image = open("image/news.jpg",mode='rb')
        resp = Response(image, mimetype="image/jpeg")
    return resp
@app.route('/',methods=['GET','POST'])
def home():
    return '''hello world'''
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run(port=9600)