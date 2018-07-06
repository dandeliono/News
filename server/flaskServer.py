from flask import Flask
from flask import request
from mong import mongoapi
import json
# -*- coding: utf-8 -*-
mongo = mongoapi();
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
@app.route('/',methods=['GET','POST'])
def home():
    pass
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