import unittest

from resource.classification import fenlei
from unit.mong import *

class TestDict(unittest.TestCase):

    def test_init(self):
        classification = fenlei();
        data = classification.titleAlldata
        self.assertTrue(isinstance(data, list))

    def test_classi(self):
        classification = fenlei();
        title = '《天才玩偶》：中国动漫迈入多元化时代的标志'
        content = '《天才玩偶》动画改编自漫画家一淳在腾讯动漫上独家连载的人气漫画《恶偶》，由腾讯动漫出品，Studio DEEN制作。'
        result = classification.classi(title,content)
        self.assertEquals(result, '动漫')

if __name__ == '__main__':
    unittest.main()