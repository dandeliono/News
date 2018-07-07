from pymongo import MongoClient
import time
import json
from unit.objectid import timestamp_from_objectid


class mongoapi:
    def __init__(self,localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

    def selectTitle(self,hash):
        data = ""
        for item in self.db.col.find({"jumpUrl":hash},{'_id':0,"title": 1}):
            print(item['title'])
            data = item['title']
        return data
    def selectDate(self,hash):
        data = ""
        for item in self.db.col.find({"jumpUrl": hash}, {'_id': 0, "time": 1}):
            print(item['time'])
            data = item['time']
        return data
    def selectFirstImg(self,hash):
        data = ""
        for item in self.db.col.find({"jumpUrl": hash}, {'_id': 0, "imgSrc": 1}):
            print(item['imgSrc'])
            data = item['imgSrc']
        return data

    def selectByHash(self,hash):
        allData = []
        for item in  self.db.col.find({"hash":hash},{ "_id": 0, "type": 1, "text": 1,"image":1,"id":1 }):
            allData.append(item)
        print(allData)
        return allData;
    def selectRepect(self,title):
        return self.db.col.find({'title': title}).count()
    def selectByType(self,type):
        allData = []
        for item in self.db.col.find({"type": type}, {"_id": 0, "type": 1, "text": 1, "image": 1, "id": 1}):
            allData.append(item)
        print(allData)
        return allData;
    def selectByLabel(self,label):
        allData = []
        for item in self.db.col.find({'label':label}):
            # print(item)
            item['_id'] = timestamp_from_objectid(item['_id'])
            # print(item['_id']);
            allData.append(item)
        print(allData)
        return allData;
    def insert(self, title,imgSrc,jumpUrl,time,type='周边',label=' '):
        if(self.selectRepect(title)):
            pass
        else:
            self.db.col.insert({'title':title,'imgSrc':imgSrc,'jumpUrl':jumpUrl,'time':time,'type':type,'label':label,'readercount':0})
    def getNewsByOpenid(self,openid):
        data = []
        newsList = ()
        i = 0
        for item in self.db.col.find({"openid": openid}, {'_id': 0, "title": 1,'label':1}):
            if(i<10):
                data.append(item)
                i = i+1
        for lab in data:
            title = lab['title']

            label = lab['label']
            newsL = self.selectByLabel(label)
            for news in newsL:
                if(news['title']!=title):
                    newsList.append(news)
        return newsList

    def delete(self,title):
        self.db.col.remove({'title':title})
    def selectByTy(self,type):
        allData = []
        for item in self.db.col.find({'type':type}):
            # print(item)
            item['_id'] = timestamp_from_objectid(item['_id'])
            # print(item['_id']);
            allData.append(item)
        print(allData)
        return allData;
    def showAll(self):
        allData = []
        for item in self.db.col.find():
            #print(item)
            item['_id'] = timestamp_from_objectid(item['_id'])
            #print(item['_id']);
            allData.append(item)
        print(allData)
        return allData;
    def remove(self):
        self.db.col.remove()
mongo = mongoapi();


class newsItem(mongoapi):
    def __init__(self, db='newsItem', localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        self.db = conn.newsItemDb
    def updateReader(self,title,readercount):
        self.db.col.update({"title": title}, {'$set': {"readercount": readercount}})
        print('修改完成')

    def updataTitleType(self,title,type):
        self.db.col.update({"title": title}, {'$set': {"type": type}})
        print('修改完成')
    def updataTitleLabel(self,title,label):
        self.db.col.update({"title": title}, {'$set': {"label": label}})
        print('修改完成')

    def selectReaderCount(self, title):
        data = []
        for item in self.db.col.find({"title": title}, {'_id': 0, "readercount": 1}):
            data.append(item)
        count = data[0]['readercount']
        print(data[0]['readercount'])
        return count


class newsDetail(mongoapi):
    def __init__(self, db='newsDetail', localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        self.db = conn.newsDetail
    def insertDetail(self,type,content,id,hash):
        if(type == 'p'):
            ty = 'text'
        else:
            ty = 'image'
        self.db.col.insert({'type':type,ty:content,'id':id,'hash':hash})
class History(mongoapi):
    def __init__(self, db='History', localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        self.db = conn.History

    def insertHistory(self, openid, title, time):
        self.db.col.insert({'openid': openid, 'title': title, 'time': time})


class Comment(mongoapi):
    def __init__(self, db='Comment', localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        self.db = conn.Comment
    def inserctCommetn(self,openid,comment,title):

        times = time.strftime("%Y-%m-%d %H:%M:%S")
        self.db.col.insert({'openid':openid,'comment':comment, 'title': title,'time':times})