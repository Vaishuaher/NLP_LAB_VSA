# Name : Vaishnavi Sanjay Aher
# Roll No. 64
# Btach : B4
# Assignment 2 : Bag of Words(BOW) Implementation with Python

import gensim
import pprint
from gensim import corpora
from gensim.utils import simple_preprocess

doc_list = [
   "It was the best of times,"
   "it was the worst of times,"
   "it was the age of wisdom,"
   "it was the age of foolishness."
]

doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
print(BoW_corpus)
id_words = [[(dictionary[id], count) for id, count in line] for line in BoW_corpus]
print(id_words)

# [[(0, 2), (1, 1), (2, 1), (3, 4), (4, 4), (5, 4), (6, 2), (7, 4), (8, 1), (9, 1)]]
# [[('age', 2), ('best', 1), ('foolishness', 1), ('it', 4), ('of', 4), ('the', 4), ('times', 2), ('was', 4), ('wisdom', 1), ('worst', 1)]]
