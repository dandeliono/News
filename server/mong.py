from pymongo import MongoClient
import json
from unit.objectid import timestamp_from_objectid
class mongoapi:
    def __init__(self, localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        self.db = conn.newsItemDb

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
    def selectRepect(self,title):
        return self.db.col.find({'title': title}).count()
    def selectByType(self,type):
        return self.db.col.find({'type':type});
    def insert(self, title,imgSrc,jumpUrl,time,type='surrounding'):
        if(self.selectRepect(title)):
            pass
        else:
            self.db.col.insert({"title":title,'imgSrc':imgSrc,'jumpUrl':jumpUrl,'time':time,'type':type})
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
