import io
from google.cloud import vision
import re
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from pattern.text.en import conjugate, lemma, lexeme, PRESENT, SG
import math
import os

import sys, json
fileptr = open("../Achesta/text.txt", "r")
content=fileptr.read()
data=[[],[],[],[]]

#data1[0]=int(input("inter maximum marks : "))
#data1[1]=int(input("enter expected_no_of_words: "))
#data1[2]=int(input("enter expected_no_of_sentences : "))
#data1[3]=input("inter keywords : ")
def get_marks(data, content):
    keywords_matched = 0
    maximum_marks = 5
    data[0]=maximum_marks

    data[3] = "domestic,animal,benefits, four-footed,horns,herbivorous,farmers"
    keywords=data[3].split(',')

    expected_keywords = len(keywords)

    expected_no_of_words = 200
    data[1]=expected_no_of_words
    expected_no_of_sentences = 15
    data[2]=expected_no_of_sentences



    # extended_keywords = []
    # for word in keywords:
    #     for syn in wn.synsets(word):
    #         for l in syn.lemmas():
    #             extended_keywords.append(l.name())

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

    keywords = [x.lower() for x in keywords]
    keywords = list(set(keywords))
    # print(keywords)

    #texts = content
   # string = texts[0].description.replace('\n', ' ').lower()  # for converting to lower case
    #string = re.sub('[^A-Za-z0-9.]+', ' ', string)  # for eliminating special character

    #print(string)

    word_list = word_tokenize(content)  # for word spliting
    no_of_words = len(word_list)
    if no_of_words > expected_no_of_words:
        no_of_words = expected_no_of_words

    no_of_sentences = len(sent_tokenize(content))
    if no_of_sentences > expected_no_of_sentences:
        no_of_sentences = expected_no_of_sentences
    print('no_of_words', no_of_words)
    print('no_of_sentences', no_of_sentences)

    for keyword in keywords:
        if (keyword in word_list):
            keywords_matched = keywords_matched + 1
    if keywords_matched > expected_keywords:
        keywords_matched = expected_keywords
    print('keywords matched', keywords_matched)

    keywords_percentage = 0.55 * (keywords_matched / expected_keywords)
    word_percentage = 0.35 * (no_of_words / expected_no_of_words)
    sentence_percentage = 0.10 * (no_of_sentences / expected_no_of_sentences)

    print('keywords_percentage', keywords_percentage)
    print('word_percentage', word_percentage)
    print('sentence_percentage', sentence_percentage)

    total_marks = maximum_marks * (keywords_percentage + word_percentage + sentence_percentage)
    total_marks = round(total_marks, 1)
    digit = total_marks * 10
    if (digit % 10 < 5):
        total_marks = math.floor(total_marks)
    if (digit % 10 > 5):
        total_marks = math.ceil(total_marks)
    print('total_marks', total_marks)
    return total_marks
print(get_marks(data, content))