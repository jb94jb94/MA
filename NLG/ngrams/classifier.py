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
import math

trump_file = "C:/Users/jbuel/OneDrive/Desktop/NLG/ngrams/8gramsO.txt"
trump_dict = {}
file = open(trump_file,"r")
trump_cont =file.read()
trump_txt=trump_cont.split('\n')
for line in trump_txt:
    line = line.replace("'","")
    (key,value) = line.split("\t")
    trump_dict[key]=value
print(str(trump_dict)[0:500])

obama_file = "C:/Users/jbuel/OneDrive/Desktop/NLG/ngrams/5gramsO.txt"
obama_dict = {}
file = open(obama_file,"r")
obama_cont =file.read()
obama_txt=obama_cont.split('\n')
for line in obama_txt:
    line = line.replace("'","")
    (key,value) = line.split(",")
    obama_dict[key]=value
print(str(obama_dict)[0:500])

for i in range(271,302):
    link = "C:/Users/jbuel/OneDrive/Desktop/NLG/Factbase/text/"+str(i)+".txt"
    dict = {}
    file= open(link,"r")
    a = str.lower(str(file.read()))
    #a = str.lower(str(json.load(file)['text']))
    ngrams = list(nltk.ngrams(a.split(),5))
    for ngram in ngrams: 
        if ngram not in dict:
            dict[ngram]=1
        else:
            dict[ngram]=dict[ngram]+1      
    file.close()
    obama=0
    trump=0
    for key in dict.keys():
        corr = str(key).replace("'","").replace("(","").replace(")","")
        #if corr in obama_dict.keys():
        obamaS = obama_dict.get(corr,1)
        
        try:
            obamaV = int(obamaS)
        except:
            print(obama_dict.get(corr,1))
        obama +=math.log(obamaV/1430213)
        #if corr in trump_dict.keys():
        trumpS = trump_dict.get(corr, 1)
        try:
            trumpV = int(trumpS)
        except:
            print(trump_dict.get(corr, 1))
        trump+=math.log(trumpV/1537146)
    print(str(obama)+":"+str(trump))

