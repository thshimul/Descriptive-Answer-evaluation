import nltk

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import gensim
from gensim import corpora,models,similarities


tokenizer= RegexpTokenizer(r'\w+')
stop_words=set(stopwords.words('english'))


fileptr1 = open('../SSHOW/data1/reference.txt', "r")
content1 = fileptr1.read()
fileptr2 = open('data/QQ2.txt', "r")
content2 = fileptr2.read()
fileptr3 = open('data/QQ3.txt', "r")
content3 = fileptr3.read()
fileptr4 = open('data/QQ4.txt', "r")
content4 = fileptr4.read()

content=[content1]
token_list=[]
for sentence in content:
    token_list.append(tokenizer.tokenize(sentence.lower()))
def remove_stopwords(words):
    filtered_word=[]
    for word in words:
        if word not in stop_words:
            filtered_word.append(word)
    return filtered_word
tokenize_data=[]
for token in token_list:
    tokenize_data.append(remove_stopwords(token))
print(tokenize_data)


dictonary=corpora.Dictionary(tokenize_data)
numerical_corpus=[dictonary.doc2bow(text) for text in tokenize_data]
lda_models=models.LdaModel(corpus=numerical_corpus,num_topics=1,id2word=dictonary)
for idx in range(1):
    print('topic #%s : '%idx,lda_models.print_topic(idx,20))
new="My name is S M towhid hasan.bangladesh is my country. i live in bangladesh.i love my country.i come from dhaka"
lda_models.get_document_topics(dictonary.doc2bow(new.split()))
lda_index=similarities.MatrixSimilarity(lda_models[numerical_corpus])
bow=dictonary.doc2bow(new.split())
similarities=lda_index[lda_models[bow]]
print(similarities)

