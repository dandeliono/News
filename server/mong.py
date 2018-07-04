from pymongo import MongoClient
class mongoapi:
    def __init__(self, localhost='localhost', port=27017):
        conn = MongoClient(localhost, port);
        self.db = conn.newsItemDb
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
    def select(self,title):
        return self.db.col.find({'title': title})
    def insert(self, title,imgSrc,jumpUrl,time):
        if(self.select(title)):
            pass
        else:
            self.db.col.insert({"title":title,'imgSrc':imgSrc,'jumpUrl':jumpUrl,'time':time})
    def delete(self,title):
        self.db.col.remove({'title':title})

    def showAll(self):
        for item in self.db.col.find():
            print(item)
    def remove(self):
        self.db.col.remove()
mongo = mongoapi();
