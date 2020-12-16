from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# print('Stemming amusing : {}'.format(ps.stem('amusing')))
print('lemmatization amusing : {}'.format(lemmatizer.lemmatize('amusing',pos = 'v')))