import json

from mong import mongoapi
from aip import AipNlp

APP_ID = '11502608'
API_KEY = 'ZfggmXPa4BakVqvZDXmZVbUY'
SECRET_KEY = 'L1ogSUqkUONDWD5RxgZveGCreTQhvxzT'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

title = "人工智能打了45万场《雷神之锤3》 水平已超过人类"

content = "自从人工智能Alphago在围棋领域战胜人类棋手之后，谷歌的人工智能DeepMind近日又在电子游戏领域超越了人类水准，一起来了解一下。"

""" 调用文章分类 """

mongoDetail = mongoapi(db='newsDetail');
mongoTitle = mongoapi();
titleAlldata = mongoTitle.showAll()
def fenlei():
    typeList = ['科技','网游','单机','硬件','影视','网游','动漫']
    for item in titleAlldata:
        print(item['title'])
        title = item['title']
        detailAlldata = mongoDetail.selectByHash(item['jumpUrl'])
        for iteme in detailAlldata:
            try:
                print(iteme['text'])
                content = iteme['text']
                result = client.topic(title, content)['item']['lv2_tag_list'][0]['tag']
                result = result.replace('游戏机','单机')
                result = result.replace('数码', '科技')
                result = result.replace('手游', '网游')
                result = result.replace('游戏', '网游')
                result = result.replace('漫画', '动漫')
                print(result)
                if result in typeList:
                    print("finsh"+result)
                    mongoTitle.updataTitleType(title,result)
                    break
            except Exception:
                pass
    print(client.topic(title, content)['item']['lv2_tag_list'][0]['tag']);
title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"

content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"

""" 调用文章标签 """
def label():
    typeList = ['科技','网游','单机','硬件','影视','网游','动漫']
    for item in titleAlldata:
        print(item['title'])
        title = item['title']
        detailAlldata = mongoDetail.selectByHash(item['jumpUrl'])
        flag = 0
        for iteme in detailAlldata:
            if(flag ==0):
                try:
                    print(iteme['text'])
                    content = iteme['text']
                    result = client.keyword(title, content)['items'][0]['tag']
                    print(result)
                    if result in typeList:
                        print("finsh"+result)
                        mongoTitle.updataTitleLabel(title,result)
                        flag = 1
                except Exception:
                    pass
fenlei()
print(client.keyword(title, content)['items'][0]['tag']);