# 新闻聚合平台
## 平台技术介绍
- 本平台使用python语言编写爬虫来获取响应的新闻
- 前端使用微信小程序技术来制作
- 后端使用机器学习技术根据获取到的文字来分类
- 通过python flask框架来实现前后端数据交互

## 平台设计开发计划
1. 微信小程序
2. 爬虫
3. 分类

### 域名：http://127.0.0.1:9600
GET http://127.0.0.1:9600/newsTitle?type=%E5%8D%95%E6%9C%BA
### 返回
```json
{
  "code": 200,
  "message": "success",
  "result": [{
      "id": 1530925445.0,
      "title": "FF\u98ce\u683cJRPG\u300a\u6c38\u6052\u8fb9\u7f18\u300b\u65b0\u56fe PC\u914d\u7f6e\u516c\u5e03\u3001\u5341\u5206\u4eb2\u6c11",
      "imgSrc": "http://127.0.0.1:9600/image/201807071037389553", "jumpUrl": "http://www.gamersky.com/news/201807/1070427.shtml", "time": "2018-07-07 10:39",
      "type": "\u5355\u673a",
      "label": " ",
      "readercount": 0
            }]
}
```
### GET /newsDetail?hash=http://www.gamersky.com/news/201807/1069906.shtml&openid=oo8zs0Llxcks9BHNhXB2vjE9K4Fs
### 返回
```json
{
  "code": 200,
  "message": "success",
  "result":
  {
    "id": "http://www.gamersky.com/news/201807/1069906.shtml",
    "title": "\u8d85\u8d5e\u300a\u590d\u80543\u300b\u98ce\u683c\u300a\u5deb\u5e083\u300b\u77ed\u7247 \u53f2\u8bd7\u7ea7\u8361\u6c14\u56de\u80a0", "date": "2018-07-06 13:22",
    "source": "",
    "firstImage": "http://127.0.0.1:9600/image/201807061037252713", "content":
    [{
      "type": "p",
      "text": "\u300a\u5deb\u5e083\u300b\u53ef\u4ee5\u8bf4\u662f\u8fd1\u5341\u5e74\u6765\u6700\u6210\u529f\u7684\u6e38\u620f\u4e4b\u4e00\uff0c\u56f4\u7ed5\u8fd9\u90e8\u6e38\u620f\u4e5f\u6709\u4e0d\u5c11\u8d28\u91cf\u6781\u9ad8\u7684\u540c\u4eba\u4f5c\u54c1\uff0c\u6bd4\u5982\u6cb9\u7ba1\u535a\u4e3bEduku\u5236\u4f5c\u7684\u4eff\u7167\u300a\u590d\u80543\uff1a\u65e0\u9650\u6218\u4e89\u300b\u98ce\u683c\u7684\u300a\u5deb\u5e083\u300b\u9884\u544a\u7247\u3002",
      "id": 0
      },
      {
        "type": "p",
        "text": "\u77ed\u7247\uff1a",
        "id": 1
        }
      ],
        "readCount": 1
        }
      }
    }
```
