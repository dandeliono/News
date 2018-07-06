from pymongo import MongoClient
import json
from unit.objectid import timestamp_from_objectid
class mongoapi:
    def __init__(self, db = 'newsItem',localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        if(db == 'newsItem'):
            self.db = conn.newsItemDb
        if(db == 'newsDetail'):
            self.db = conn.newsDetail
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
        return self.db.col.find({'type':type});
    def insert(self, title,imgSrc,jumpUrl,time,type='surrounding'):
        if(self.selectRepect(title)):
            pass
        else:
            self.db.col.insert({"title":title,'imgSrc':imgSrc,'jumpUrl':jumpUrl,'time':time,'type':type})
    def insertDetail(self,type,content,id,hash):
        if(type == 'p'):
            ty = 'image'
        else:
            ty = 'text'
        self.db.col.insert({'type':type,ty:content,'id':id,'hash':hash})
    def delete(self,title):
        self.db.col.remove({'title':title})

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
