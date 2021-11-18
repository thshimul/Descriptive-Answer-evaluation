from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
from nltk.corpus import wordnet as wn
from pattern.text.en import conjugate, lemma, lexeme, PRESENT, SG
import math
import spacy

"""keywords_matched=0
data1=[[]]
data1[0] = "domestic,animal,benefits,four-footed,horns,herbivorous,farmers"
keywords=data1[0].split(',')
print(keywords)
forms = []  # We'll store the derivational forms in a set to eliminate duplicates
wordnet_lemmatizer = WordNetLemmatizer()
for w in keywords:
    forms.append(lemma(w))
verb = []
for word in keywords:
        verb.extend(lexeme(word))
keywords.extend(forms)
keywords.extend(verb)

forms = []  # We'll store the derivational forms in a set to eliminate duplicates
for word in keywords:
    for happy_lemma in wn.lemmas(word):  # for each "happy" lemma in WordNet
        forms.append(happy_lemma.name())  # add the lemma itself
        for related_lemma in happy_lemma.derivationally_related_forms():  # for each related lemma
            forms.append(related_lemma.name())  # add the related lemma

verb = []
for word in keywords:
    verb.extend(lexeme(word))

# keywords.extend(extended_keywords)
keywords.extend(forms)
keywords.extend(verb)
print(keywords)
fileptr = open("../Achesta/data1.txt", "r")
content=fileptr.read()
print(content)
word_list = word_tokenize(content)
for keyword in keywords:
    if (keyword in word_list):
        keywords_matched = keywords_matched + 1
print(keywords_matched)
extended_keywords = []

for word in keywords:
	for syn in wn.synsets(word):
		for l in syn.lemmas():
			extended_keywords.append(l.name())

extended_keywords = list(set(extended_keywords))
print (extended_keywords)
forms=[]
for happy_lemma in wn.lemmas("mine"):
    forms.append(happy_lemma.name())

print(forms)
print(wn.lemmas("mine"))"""
spacy.load("en_core_web_md")