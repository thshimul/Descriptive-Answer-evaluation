import io
import re
import nltk
from nltk import sent_tokenize,word_tokenize
from nltk.corpus import wordnet as wn
from pattern.text.en import conjugate, lemma, lexeme,PRESENT,SG
import math
import os

data=[[],[],[],[]]

#data1[0]=int(input("inter maximum marks : "))
#data1[1]=int(input("enter expected_no_of_words: "))
#data1[2]=int(input("enter expected_no_of_sentences : "))
data[3]=input("inter keywords : ")
keywords=data[3].split(',')
#keywords="domestic,animal,benefits, four-footed,horns,herbivorous,farmers"
extended_keywords = []

for word in keywords:
	for syn in wn.synsets(word):
		for l in syn.lemmas():
			extended_keywords.append(l.name())

extended_keywords = list(set(extended_keywords))
print(extended_keywords)


