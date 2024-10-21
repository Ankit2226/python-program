from nltk.steam import WordNetLemmatizer

Lemmatizer = WordNetLemmatizer()

print("rocks :",Lemmatizer.lemmatize("rocks"))
print("object :",Lemmatizer.lemmatize("object"))

print("better :",Lemmatizer.lemmatize("better",pos="e"))