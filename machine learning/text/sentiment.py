
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from math import fabs
sa = SentimentIntensityAnalyzer()
fileptr1 = open('text.txt', "r")
content1 = fileptr1.read()
fileptr2 = open('data/New Text Document.txt', "r")
content2 = fileptr2.read()
dic1=sa.polarity_scores(content1)
dic2=sa.polarity_scores(content2)
print(dic1)
print(dic2)
com1=dic1['neg']
com2=dic2['neg']
print(com1)
print(com2)
dif=(com1-com2)
print(dif)
print(fabs(dif))