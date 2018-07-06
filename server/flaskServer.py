from flask import Flask,Response,render_template, jsonify
from flask import request
from mong import mongoapi
import json
# -*- coding: utf-8 -*-
mongo = mongoapi();
mongoDetail = mongoapi(db='newsDetail')
app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

@app.route('/newsTitle', methods=['GET', 'POST'])
def newsTitle():
    searchword = request.args.get('type', '')
    print("serachword"+searchword);
    if request.method == 'GET':
        newsList = mongo.showAll()
    print(newsList)
    newsTitle = {
        "code": 200,
        "message":"success",
        "result":newsList
    }

    return json.dumps(newsTitle);
@app.route('/newsDetail',methods=['GET','POST'])
def newsDetail():
    searchword = request.args.get('hash', '')
    print("serachword" + searchword);
    newsList = mongoDetail.selectByHash(searchword)
    title = mongo.selectTitle(searchword)
    date = mongo.selectDate(searchword)
    firstImage = mongo.selectFirstImg(searchword)
    result ={
        "id":searchword,
        "title":title,
        "date":date,
        "source":"",
        "firstImage": firstImage,
        "content":newsList
    }
    newsDetail={
        "code":200,
        "message":"success",
        "result":result
    }
    print(newsDetail)
    return json.dumps(newsDetail)
@app.route("/image/<imageid>")
def index(imageid):
    print(imageid)
    image = open("image/{}.jpg".format(imageid),mode='rb')
    print(image)
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