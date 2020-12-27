import re
import numpy as np


#字詞前處理
#定義簡易文本資料(使用Ch17講義中的例子)
corpus = ['You say goodbye and I say hello.']
word_dict = set()
processed_sentence = []
for sentence in corpus:
    #將所有字詞轉為小寫
    sentence = sentence.lower()
    #移除標點符號(可以依據使用狀況決定是否要移除標點符號)
    pattern = r'[^\W_]+'
    sentence = re.findall(pattern, sentence)
    #添加字詞到字典中
    word_dict |= set(sentence)
    processed_sentence.append(sentence)
# print(processed_sentence)

#建立字詞ID清單
word2idx = dict()
idx2word = dict()
for word in word_dict:
    if word not in word2idx:
        idx = len(word2idx)
        word2idx[word] = idx
        idx2word[idx] = word
#將文本轉為ID型式
id_mapping = lambda x: word2idx[x]
corpus = np.array([list(map(id_mapping, sentence)) for sentence in processed_sentence])
# print(corpus)
# print(word2idx)
# print(idx2word)


# 共現矩陣
#定義共現矩陣函式
vocab_size = len(word2idx)
window_size = 1
# initialize co-occurrence matrix
co_matrix = np.zeros(shape=(vocab_size, vocab_size), dtype=np.int32)
for sentence in corpus:
    sentence_size = len(sentence)
    for idx, word_id in enumerate(sentence):
        for i in range(1, window_size+1):
            left_idx = idx-i
            right_idx = idx+i

            if left_idx>=0:
                left_word_id = sentence[left_idx]
                co_matrix[word_id, left_word_id] += 1
            if right_idx<sentence_size:
                right_word_id = sentence[right_idx]
                co_matrix[word_id, right_word_id] += 1
# print(co_matrix)


# 定義餘弦相似度
def cos_similarity(x: np.ndarray, y: np.ndarray, eps: float=1e-8):
    nx = x / (np.sqrt(np.sum(x**2)) + eps)
    ny = y / (np.sqrt(np.sum(y**2)) + eps)
    
    return np.dot(nx,ny)

# calculate the similarity between I and you
cossimilarity = cos_similarity(co_matrix[word2idx['i']], co_matrix[word2idx['you']])
# print(cossimilarity)

# 正向點間互資訊(PPMI)
M = np.zeros_like(co_matrix, dtype=np.float32)
N = np.sum(co_matrix)
S = np.sum(co_matrix, axis=0)
total = co_matrix.shape[0]*co_matrix.shape[1]
    
for i in range(co_matrix.shape[0]):
    for j in range(co_matrix.shape[1]):
        pmi = np.log2(co_matrix[i, j]*N / (S[i]*S[j]))
        M[i, j] = max(0, pmi)
# print(M)

# 奇異值分解(SVD)
# 使用np的linalg.svd對PPMI矩陣進行奇異值分解

# SVD
U, S, V = np.linalg.svd(M)

# 使用SVD將將原本的稀疏向量轉變為稠密向量
print(f'hello in co-occurrence matrix: {co_matrix[0]}')
print(f"hello in PPMI: {M[0]}")
print(f"hello in SVD: {U[0]}")