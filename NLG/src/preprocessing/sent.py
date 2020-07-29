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

current_dir = "C:/Users/jbuel/OneDrive/Desktop/NLG"
dict = {}

sent = 0
for i in range(1,474):
    try:
        fileLoc = current_dir + "/AmRhet/text/"+str(i)+".txt"
        file= open(fileLoc,"r")
        a = str.lower(str(json.load(file)['text']))  
        sent = sent+a.count(".")+1
        file.close()
    except:
        print(sys.exc_info()[0])
print(sent)