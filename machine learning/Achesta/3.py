import io
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.stem import PorterStemmer
fileptr = open("text.txt","r")
content=fileptr.read()
print(content)
word_list = word_tokenize(content)
print(word_list)
ps=PorterStemmer()
for w in word_list:
	rootWord=ps.stem(w)
	print(rootWord)
wordnet_lemmatizer = WordNetLemmatizer()
for w in word_list:
		print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))