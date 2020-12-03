from ckiptagger import data_utils, WS
# data_utils.downlaod_data_gdown('./') # 太多人下載,直接網頁下載


#建構斷詞
# ws = WS("./data/big/data")
# input_string = '小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造'
# word_sentence_list = ws(
#     input_string,
#     sentence_segmentation = True, # To consider delimiters 考慮定界符
#     segment_delimiter_set = {",", "。", ":", "?", "!", ";"} # This is the defualt set of delimiters
# )
# print(word_sentence_list)


# 使用 Ckiptagger 詞性標注
# from ckiptagger import POS
# pos = POS("./data/big/data")
# pos_sentence_list = pos(word_sentence_list)
# print(pos_sentence_list)

# 使用 Ckiptagger 命名實體識別
# from ckiptagger import NER
# ner = NER("./data/big/data")
# entity_sentence_list = ner(word_sentence_list, pos_sentence_list)
# print(entity_sentence_list)

# 將自定義字典加入斷詞器中
from ckiptagger import construct_dictionary
word_to_weight = {"日本東京大學": 1}
dictionary = construct_dictionary(word_to_weight)
# 建構斷詞器
ws = WS("./data/big/data")
input_traditional_str = ['小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造']
word_sentence_list = ws(input_traditional_str, recommend_dictionary=dictionary)
print(word_sentence_list)
