'''
Created on 12.03.2020

@author: jbuel
'''
import os
import collections
from symbol import except_clause
import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from builtins import dict
import json
import re
import string

from gensim.models import Word2Vec

#nltk.download('punkt')
#nltk.download("stopwords")

current_dir = "C:/Users/jbuel/OneDrive/Desktop/NLG"

data = []
for i in range(1,430):
    fileLoc = current_dir + "/AmRhet/text/"+str(i)+".txt"
    file= open(fileLoc,"r")
    a = str.lower(str(json.load(file)['text']))
    a = re.sub(r'[^\w\s]','',a)

    #a = str.lower(str(file.read()))
    #a = re.sub(r'[^\w\s]','',a)
    
    for sentence in tokenize.sent_tokenize(a):
        sent = []
        for word in tokenize.word_tokenize(sentence):
            if word.isalpha():
               # if word not in stopwords.words('english'):
               sent.append(word)
        data.append(sent)  
        file.close()
#print(data)
print(len(data))
    #a = re.sub(r'[^\w\s]','',a)

word2vec = Word2Vec(data, min_count=2)
#vocabulary = word2vec.wv.vocab
#print(vocabulary)
sim_words = word2vec.wv.most_similar('refugee')
print(sim_words)
