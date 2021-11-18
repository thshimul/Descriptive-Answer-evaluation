import spacy
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import gensim
import glob
from math import fabs

from werkzeug.utils import secure_filename

nlp = spacy.load('en_core_web_md')





# SENTIMENT ANALYSIS
def sentiment_analysis(con1,con2):
    print('student answer :' , con1)
    print('reference answer :' , con2)
    sa = SentimentIntensityAnalyzer()
    dic1=sa.polarity_scores(con1)
    dic2=sa.polarity_scores(con2)
    print('sentiment analysis')
    print('student answer :',dic1)
    print('reference answer :',dic2)
    com1=dic1['neg']
    com2=dic2['neg']

    dif=(com1-com2)
    print('change of negative sentiment :',fabs(dif))
    return fabs(dif)

# Keyword Analysis.
def kewword_analysis(con1,con2,data):
    doc1 = nlp(con1)
    doc2 = nlp(con2)
    number_words1 = len(doc1)
    number_sentence1 = len(list(doc1.sents))
    number_words_check = len(doc2)
    number_sentence_check = len(list(doc2.sents))
    data.append(number_words1)
    data.append(number_sentence1)
    keyword = []

    keyword = data[0].split(',')
    Question_marks = data[2]
    keywords_number = len(keyword)
    lst = [[] for _ in range(keywords_number)]
    k = 0
    for k in range(keywords_number):
        lst[k].append(keyword[k])

    synonyms = [[] for _ in range(keywords_number)]
    i = 0
    for s in lst:
        for k in s:
            for x in wordnet.synsets(k):
                for l in x.lemmas():
                    synonyms[i].append(l.name())
        i += 1

    print(synonyms)

    token_list = []
    for token in doc1:
        token_list.append(token.lemma_)
    print(token_list)

    count = 0
    for k in synonyms:
        for x in k:
            if (x in token_list):
                count = count + 1
                break

    matched_keyword=count
    print("matched keyword",matched_keyword)

    print("keyword_number", keywords_number)
    if  matched_keyword>=keywords_number:
        kw_number=0.60*1
    else:
        kw_number=0.60* ( matched_keyword/keywords_number)

    if  number_words1>=number_words_check:
        word_number=0.30*1
    else:
        word_number=0.30* (number_words1/number_words_check)
    if  number_sentence1>=number_sentence_check:
        sentence_number=0.10*1
    else:
        sentence_number=0.10* (number_sentence1/number_sentence_check)


    marks_obtain = Question_marks* (kw_number+ word_number + sentence_number)
    print(" keyword basis mark : ",kw_number)
    print(" word basis mark : ",word_number)
    print(" sentence basis mark: ",sentence_number)
    print(" number of words in student answer : ",number_words1)
    print(" number of words in reference answer : ",number_words_check)
    print(" matches are : ",count)
    print(" normal doc similarity : ",doc1.similarity(doc2))
    print(" marks basis on keyword analysis : ",marks_obtain)
    return marks_obtain

#SEMANTIC ANALYSIS:
def semantic_analysis(con11,data):
    files=glob.glob("data1/*.txt")
    doc=[]
    for file in files:
        try:
            with open (file, "r", encoding="utf-8") as f:
                doc.append(f.read())
        except:
            pass


    print('semantic analysis')
    remove_stopwords=[]
    for text in doc:
        remove_stopwords.append(gensim.utils.simple_preprocess(text))
    print(" after removing stop words : ",remove_stopwords)
    dictionary = gensim.corpora.Dictionary(remove_stopwords)
    print("Number of words in dictionary:",len(dictionary))
    for i in range(10):
        print(i, dictionary[i])
    corpus = [dictionary.doc2bow(text) for text in remove_stopwords]
    print(corpus[:10])


    tf_idf = gensim.models.TfidfModel(corpus)
    print("term frequency and inverse term frequency : ",tf_idf)
    similarity_object = gensim.similarities.Similarity('data1/', tf_idf[corpus], num_features=len(dictionary))

    print(similarity_object)



    examine_data=con11
    print(" examine data : ",examine_data)
    query_doc = gensim.utils.simple_preprocess(examine_data)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    similarity_scores=list(similarity_object[query_doc_tf_idf])
    print(" semantic similarity :   ",similarity_scores)

    similarity=max(similarity_scores)
    marks=data[2]*similarity
    print (marks)
    return marks


def calculated_marks(st,kw,sm):
    if st<.15:
        """ffmarks=(kw+sm)/2
        fmarks=ffmarks
        print(" marks calculation :   ",fmarks)
        #digit = fmarks * 10
        '''if (digit % 10 < 5):
            final_marks = math.floor(marks)
        if (digit % 10 > 5):
            final_marks = math.ceil(marks)
        print(" final  marks  :   ", final_marks)'''
        return fmarks"""
        return kw,sm
    else:
        print(" student answer sentiment is not good")

def must_sentence(marks,data,con):
    doc1 = nlp(con)
    mwords=data[1]
    doc2=nlp(mwords)
    token_list = []
    for token in doc1:
        token_list.append(token.text)
    chelist=[]
    for token in doc2:
        chelist.append(token.lemma_)
    co=len(chelist)
    count=0
    for k in chelist:
        if (k in token_list):
            count = count + 1
    print(" sentence's word number : ",co)
    print(" sentence's matched  word number : ", count)
    if  count>=co:
        fco=count
    else:
        fco=count
    if co!=0:
        mcal=fco/co
    else:
        mcal="no important sentence"

    return mcal


from flask import *

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f1 = request.files['student_file']
        f2 = request.files['reference_file']
        if f1:
            f1.save(f1.filename)

            fileptr1 = open(f1.filename, "r",encoding="utf-8")
            content1 = fileptr1.read()
        if f2:
            filename = secure_filename(f2.filename)
            f2.save(filename)
            fileptr2 = open(filename, "r",encoding="utf-8")
            content2= fileptr2.read()


        data = [request.form['keywords'],request.form['important sentence'],int(request.form['Question_marks'])]
        print(data)
        sentiment=sentiment_analysis(content1,content2)
        keyword=kewword_analysis(content1,content2,data)
        semantic = semantic_analysis(content1,data)

        marks=calculated_marks(sentiment,keyword,semantic)

        fmarks=must_sentence(marks,data,content1)


        return render_template('results.html', smarks=semantic,kmarks=keyword,imsen=fmarks)











if __name__ == '__main__':
    app.run(debug=True)




