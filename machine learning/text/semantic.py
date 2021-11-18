import gensim


import glob
file_names=glob.glob("data/*.txt")


raw_documents=[]
for file in file_names:
    try: # we'll use try-catch block to prevent the code from crashing if it cannot read any of the txt files
        with open (file, "r", encoding="utf-8") as f:
            raw_documents.append(f.read())
    except:
        pass
print(raw_documents)
print("Number of documents:",len(raw_documents))
clean_texts=[]
for text in raw_documents:
    clean_texts.append(gensim.utils.simple_preprocess(text))
print(clean_texts)
dictionary = gensim.corpora.Dictionary(clean_texts)

print("Number of words in dictionary:",len(dictionary))

# lets see the first 100 words from the dictionary
for i in range(10):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(text) for text in clean_texts]
print(corpus[:10]) # print first 10 bags of words
# Now we create a tf-idf model from the corpus.
# The num_nnz parameter that we'll see in the output is the number of tokens.

tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
similarity_object = gensim.similarities.Similarity('data/', tf_idf[corpus], num_features=len(dictionary))
# 'bbc_sport/'>> we're specifying the folder that the similarity index object will be stored
print(similarity_object)
print(type(similarity_object))

fileptr = open("../SSHOW/answer1.txt", "r")
q_text=fileptr.read()
print(q_text)
query_doc = gensim.utils.simple_preprocess(q_text)
# printing out the bag of words
query_doc_bow = dictionary.doc2bow(query_doc)
print(query_doc_bow)
# getting the tfidf vector
query_doc_tf_idf = tf_idf[query_doc_bow]
print(query_doc_tf_idf)
similarity_scores=list(similarity_object[query_doc_tf_idf])
print(similarity_scores)

max_score=max(similarity_scores)

print (max_score)