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

current_dir = "C:/Users/jbuel/OneDrive/Desktop/NLG"

sent = 0
for i in range(1,302):
    try:
            fileLoc = current_dir + "/Factbase/text/"+str(i)+".txt"
            file= open(fileLoc,"r")
            a = str.lower(str(file.read()))
            sent = sent + a.count(".")+1
            file.close()
    except:
        print(sys.exc_info()[0])
print(sent)