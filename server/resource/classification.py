from aip import AipNlp

from unit.mong import *
from abc import ABCMeta, abstractmethod

class NB:
    __metaclass__ = ABCMeta

    def __init__(self):
        APP_ID = '11502608'
        API_KEY = 'ZfggmXPa4BakVqvZDXmZVbUY'
        SECRET_KEY = 'L1ogSUqkUONDWD5RxgZveGCreTQhvxzT'

        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

        #mongoDetail = mongoapi(db='newsDetail');
        self.mongoDetail = newsDetail();
        #mongoTitle = mongoapi();
        self.mongoTitle = newsItem;
        self.titleAlldata = self.mongoTitle.showAll()

    @abstractmethod
    def fenleis(self):
        pass

    @abstractmethod
    def classi(self):
        pass


class fenlei(NB):
    def fenleis(self):
        typeList = ['科技','网游','单机','影视','网游','动漫']
        for item in self.titleAlldata:
            print(item['title'])
            title = item['title']
            detailAlldata =self.mongoDetail.selectByHash(item['jumpUrl'])
            for iteme in detailAlldata:
                try:
                    print(iteme['text'])
                    content = iteme['text']
                    result = self.client.topic(title, content)['item']['lv2_tag_list'][0]['tag']
                    result = result.replace('游戏机','单机')
                    result = result.replace('数码', '科技')
                    result = result.replace('手游', '网游')
                    result = result.replace('游戏', '单机')
                    result = result.replace('漫画', '动漫')
                    print(result)
                    if result in typeList:
                        print("finsh"+result)
                        self.mongoTitle.updataTitleType(title,result)
                        break
                except Exception:
                    pass
        #print(client.topic(title, content)['item']['lv2_tag_list'][0]['tag']);
    def classi(self,title,content):
        type = self.client.topic(title, content)['item']['lv2_tag_list'][0]['tag'];
        return type
class label(NB):
    def fenleis(self):
        typeList = ['科技','网游','单机','硬件','影视','网游','动漫']
        for item in self.titleAlldata:
            print(item['title'])
            title = item['title']
            detailAlldata = self.mongoDetail.selectByHash(item['jumpUrl'])
            flag = 0
            for iteme in detailAlldata:
                if(flag ==0):
                    try:
                        print(iteme['text'])
                        content = iteme['text']
                        result = self.client.keyword(title, content)['items'][0]['tag']
                        print(result)
                        if result in typeList:
                            print("finsh"+result)
                            self.mongoTitle.updataTitleLabel(title,result)
                            flag = 1
                    except Exception:
                        pass

    def classi(self, title, content):
        type = self.client.topic(title, content)['item']['lv2_tag_list'][0]['tag'];
        return type


if __name__ == '__main__':
    nb = fenlei();
    nb.fenleis();