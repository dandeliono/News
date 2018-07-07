import jieba.analyse
def splite(text):
#第一步：分词，这里使用结巴分词全模式
 fenci_text = jieba.cut(text)
 print("/ ".join(fenci_text))
#第二步：去停用词
#这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
 stopwords = {}.fromkeys([ line.rstrip() for line in open('resource/stopwords.txt') ])
 final = ""
 for word in fenci_text:
    if word not in stopwords:
        if (word != "。" and word != "，") :
            final = final + " " + word
 print(final)
#第三步：提取关键词
 a=jieba.analyse.extract_tags(text, topK = 5, withWeight = True, allowPOS = ("n"))
 print(a)
 return

text = '''每到夏日，海边总会让人心驰神往，因为那里不仅有清凉的海风，更有阳光、沙滩、和比基尼！今天小编就来分享一下近期日本网友评选的「绝赞泳装女艺人」，一起来看看这些穿上泳装让人受不了的女星，都有谁吧？
'''
splite(text)
#text 为待提取的文本
# topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
# withWeight:是否一并返回关键词权重值，默认值为False。
# allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。