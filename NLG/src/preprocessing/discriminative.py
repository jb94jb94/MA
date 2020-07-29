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
from scipy.spatial import ckdtree

root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.curdir)))
print(root)

#obama
obama1gram_dict = {}
f = open(root+"/ngrams/1gramsO.txt","r")
obama = f.read()
obama1gram=obama.split('\n')
for line in obama1gram:
    line = line.replace("'","")
    (key,value) = line.split("\t ")
    obama1gram_dict[key]=value
    
countKeys = len(obama1gram_dict)
countValues = 0
for key,value in obama1gram_dict.items():
    countValues =countValues+int(value)

#normalize
obama1gram_dictN = {}
for key,value in obama1gram_dict.items():
    obama1gram_dictN[key]=int(value)/countValues

#trump
trump1gram_dict = {}
f = open(root+"/ngrams/1gramsT.txt","r")
trump = f.read()
trump1gram=trump.split('\n')
for line in trump1gram:
    line = line.replace("'","")
    (key,value) = line.split("\t ")
    trump1gram_dict[key]=value
    
countKeys = len(trump1gram_dict)
countValues = 0
for key,value in trump1gram_dict.items():
    countValues =countValues+int(value)
print(countKeys)
print(countValues)

#normalize
trump1gram_dictN = {}
for key,value in trump1gram_dict.items():
    trump1gram_dictN[key]=int(value)/countValues

intersect=[]
for key in obama1gram_dictN.keys():
    if key in trump1gram_dictN:
        intersect.append(key)
for key in trump1gram_dictN.keys():
    if key in obama1gram_dictN:
        intersect.append(key)
intersect=list(set(intersect))

discrim_dict = {}
for i in intersect:
    discrim_dict[i]=obama1gram_dictN[i]/trump1gram_dictN[i]
print(str(discrim_dict)[0:500])

dd_most = sorted(discrim_dict.items(),key=lambda x:x[1],reverse=True)
dd_least = sorted(discrim_dict.items(),key=lambda x:x[1])

print(str(dd_most)[0:500])
print(str(dd_least)[0:500])

#pretty printing
output = str(dd_most).replace(", (","\n")
output = output.replace("[","")
output = output.replace("]","")
output = output.replace("' , ","\t")
output = output.replace("(","")
    
f = open(root+"/ngrams/discrim.txt","w")
f.write(output)
f.close()

f.close()
