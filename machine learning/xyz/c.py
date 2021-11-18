from nltk.corpus import wordnet

#nlp = spacy.load('en_core_web_md')
#from spacy.matcher import PhraseMatcher
#matcher = PhraseMatcher(nlp.vocab)

keywords = ['want','study']
k=len(keywords)
synonyms =[]

first = []
second=[]

for i in range(0,k):
    s = keywords[i]


    for syn in wordnet.synsets(s):

        for l in syn.lemmas():

            first.append(l.name())
    synonyms.append(first)
    first.clear()






print(synonyms)