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
import string 

current_dir = "C:/Users/jbuel/eclipse-workspace/PresidentalCrawler"

for j in range(1,10):
    dict = {}
    cNgrams = 0
    for i in range(1,270):
        try:
            fileLoc = current_dir + "/Factbase/text/"+str(i)+".txt"
            file= open(fileLoc,"r")
            a = str.lower(str(file.read()))
            a = re.sub(r'[^\w\s]','',a)
            ngrams = list(nltk.ngrams(a.split(),j))
            cNgrams += len(ngrams)
            for ngram in ngrams:
                if ngram not in dict:
                    dict[ngram]=1
                else:
                    dict[ngram]=dict[ngram]+1      
                    file.close()
        except:
            print(sys.exc_info()[0])
    dict_s = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    print(len(dict_s))
    dict_s = str(dict_s).replace(", ((","\n")
    dict_s = dict_s.replace("((", "")
    dict_s = dict_s.replace("[","")
    dict_s = dict_s.replace("]","")
    dict_s = dict_s.replace(")", "")

    f = open(str(j)+"gramsT.txt","w")
    print(str(j)+"::"+str(cNgrams))
    f.write(str(dict_s))
    f.close()