import unittest
from resource.classification import fenlei
from GSpider import xkSpider
from unit.mong import *


class TestDict(unittest.TestCase):
    def test_init(self):
        classification = fenlei()
        data = classification.titleAlldata
        self.assertTrue(isinstance(data, list))

    def test_classi(self):
        classification = fenlei()
        title = '《天才玩偶》：中国动漫迈入多元化时代的标志'
        content = '《天才玩偶》动画改编自漫画家一淳在腾讯动漫上独家连载的人气漫画《恶偶》，由腾讯动漫出品，Studio DEEN制作。'
        result = classification.classi(title, content)
        self.assertEquals(result, '动漫')


class TestSpider(unittest.TestCase):
    def test_init(self):
        url = 'http://www.gamersky.com/news/'
        xkSpiders=xkSpider(url)
        self.assertTrue(isinstance(xkSpiders,object))

    def test_spider(self):
        url = 'http://www.gamersky.com/news/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/62.0.3202.94 Safari/537.36',
            'Referer': url,
        }
        xkSpiders = xkSpider(url)
        self.assertTrue(xkSpiders.xkspider())


class TestMong(unittest.TestCase):
    def test_init(self):
        mongs = mongoapi()
        self.assertTrue(isinstance(mongs, object))

    def test_news(self):
        mongs = newsItem
        self.assertTrue(isinstance(mongs, object))


if __name__ == '__main__':
    unittest.main()