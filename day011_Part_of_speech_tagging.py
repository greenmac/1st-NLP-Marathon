import jieba

'''
# jieba 斷句
sentence_1 = "我愛寫程式"
sentence_2 = "Python是一種廣泛使用的直譯式、進階程式、通用型程式語言"
print("output 精確模式: {}".format('|'.join(jieba.cut(sentence_1, cut_all=False, HMM=False))))
print("output 全模式: {}".format('|'.join(jieba.cut(sentence_1, cut_all=True, HMM=False))))
'''
'''
# jieba 新增單詞
sentence_1 = "精通各種程式語言是一件相當困難的事情"
print("output 精確模式: {}".format('|'.join(jieba.cut(sentence_1, cut_all=False, HMM=False))))
jieba.add_word('程式語言')
print("output 精確模式: {}".format('|'.join(jieba.cut(sentence_1, cut_all=False, HMM=False))))
'''
'''
# 讀入字典新增單詞
## 新增單詞 ，格式：每行包含一個單詞 詞頻(可省略) 詞性(可省略)
new_words = '程式語言\nCupoy平台\n自然語言處理'
with open('./data/new_words.txt', 'w', encoding='utf-8') as file:
	file.write(new_words)
sentence_1 = "我在Cupoy平台上學習自然語言處理"
print("output 精確模式: {}".format('|'.join(jieba.cut(sentence_1, cut_all=False, HMM=False))))
## 讀入字典
jieba.load_userdict('./data/new_words.txt')
sentence_1 = "我在Cupoy平台上學習自然語言處理"
print("output 精確模式: {}".format('|'.join(jieba.cut(sentence_1, cut_all=False, HMM=False))))
'''
'''
# Tokenize：可以用來取出斷詞位置
sentence_2 = 'Python是一個廣泛使用的直譯式、進階程式、通用型程式語言'
words = jieba.tokenize(sentence_2,)
for tk in words:
	print("word: {},        start:{}, end:{}".format(tk[0],tk[1],tk[2]))
'''
'''
# Pos Tagging
import jieba.posseg as pseg
sentence_2 = "Python是一種廣泛使用的直譯式、進階程式、通用型程式語言"
words = pseg.cut(sentence_2,)
## 對應詞性可在此網頁查詢：https://www.cnblogs.com/chenbjin/p/4341930.html
for word, flag in words:
	print(word, flag)
'''

# tokenize / Tagging
import nltk
sentence = 'Wow... Loved this place.'
tokenize = nltk.word_tokenize(sentence)
print('Token: {}'.format('|'.join(tokenize)))
tagging = nltk.pos_tag(tokenize,)
print(tagging)