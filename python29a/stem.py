from nltk.Steam import porterStemmer
from nltk.tokenize import word_tokenize
ps=porterStemmer()
words =["running","runner","ran","runs"]
for w in words:
    print(w,":",ps.stem(w))
    