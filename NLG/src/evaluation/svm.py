'''
Created on 12.03.2020

@author: jbuel
'''
import os
import collections
from symbol import except_clause
import nltk
from builtins import dict
import json
import re
import sys
import os
import numpy as np
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import random
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.curdir)))
X = []
y = []
for i in range(1,474):
    #take = random.randint(1,474)
    #if (take<=309):
    fileLoc = "./AmRhet/text/"+str(i)+".txt"
    file= open(fileLoc,"r",encoding='utf-8',errors='ignore')#   
    a = str.lower(str(json.load(file)['text']))
    a = re.sub(r'[^\w\s.]','',a)
    for sent in a.split('.'):
        if len(sent)>5:     
            take = random.randint(0,86430)
            if take<=10000:
                X.append(sent)
                y.append(0)    
    file.close()
#downsampling needed
print(len(X))

for i in range(1,309):
    fileLoc = "./Factbase/text/"+str(i)+".txt"
    file= open(fileLoc,"r",encoding='utf-8',errors='ignore')
    a = str.lower(str(json.load(file)['text']))
    a = re.sub(r'[^\w\s.]\n','',a)
    for sent in a.split('.'):
        if len(sent)>5:
            take = random.randint(1,141705)
            if take<=10000:
                X.append(sent)
                y.append(1)    
    file.close()
print(X[0:5])
print(y)

tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(X).toarray()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

classifier = svm.SVC()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))