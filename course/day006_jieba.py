import jieba
import jieba.posseg as pseg

# print(jieba.__file__) # 找到jieba路徑

jieba.set_dictionary('./data/dict.txt.big') # 設定使用字典
jieba.load_userdict("./data/userdict.txt")
jieba.add_word("國立臺灣大學")
jieba.suggest_freq("國立臺灣大學", True) # 動態調整詞頻
'''
input_string = '小明碩士畢業於國立台灣大學，現在在日本東京大學進修深造'
cutted_words = jieba.cut(input_string)
words = [word for word in cutted_words]
print(words)
'''
'''
input_string = '他来到了网易杭研大厦'
cutted_words = jieba.cut(input_string, HMM=True)
words = [word for word in cutted_words]
print(words)
'''
'''
input_str = "小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造"
cutted_words = pseg.cut(input_str) # 可參考POS 對照表
words = [(words, flag) for (words, flag) in cutted_words]
print(words)
'''

# 進行詞性標注(PoS Tagging)
input_str = u'小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造' #在此將字串轉為unicode
words = jieba.tokenize(input_str)
for tk in words:
    print(f'words:{tk[0]}, start:{tk[1]}, end:{tk[2]}')
# words_list = [(tk[0], tk[1], tk[2]) for tk in words] # append list
# print(words_list)