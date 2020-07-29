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
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.curdir)))

for n in range(1,10):
    dict = {}
    for i in range(1,309):
        try:
            fileLoc = root+"/Factbase/text/"+str(i)+".txt"
            file= open(fileLoc,"r")
            a = str.lower(str(json.load(file)['text']))
            a = re.sub(r'[^\w\s]','',a)
            ngrams = list(nltk.ngrams(a.split(),n))
            #cNgrams += len(ngrams)
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
    dict_s = dict_s.replace("'),","'\t")
    dict_s = dict_s.replace(",),","\t")
    dict_s = dict_s.replace(")", "")
    
    f = open(root+"/ngrams/"+str(n)+"gramsT.txt","w")
    #print(str(n)+"::"+str(cNgrams))
    f.write(str(dict_s))
    f.close()