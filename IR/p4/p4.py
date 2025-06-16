#AIM: Write a program to Compute Similarity between  two  text documents. 

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

#word_tokenize accepts a string as an input, not a file. 
stop_words = set(stopwords.words('english')) 
file1 = open("C:\\Users\\CS\\Desktop\\IR Pracs\\p4\\file1.txt") 
line = file1.read()# Use this to read file content as a stream: 
words = line.split() 
appendFile = open('filteredtext.txt','w') 
for r in words: 
    if not r in stop_words: 
        appendFile.write(" "+r) 
appendFile.close() 
file2 = open("C:\\Users\\CS\\Desktop\\IR Pracs\\p4\\file2.txt") 
line = file2.read()# Use this to read file content as a stream: 
words = line.split() 
appendFile = open('filteredtext1.txt','w') 
for r in words: 
    if not r in stop_words: 
        appendFile.write(" "+r) 
appendFile.close() 
file3 = open("C:\\Users\\CS\\Desktop\\IR Pracs\\p4\\file3.txt") 
line = file3.read()# Use this to read file content as a stream: 
words = line.split() 
appendFile = open('filteredtext2.txt','w') 
for r in words: 
    if not r in stop_words: 
        appendFile.write(" "+r) 
appendFile.close() 

file1=open("filteredtext.txt","r")
file2=open("filteredtext1.txt","r")
file3=open("filteredtext2.txt","r")
doc1=[file1.read(),file2.read(),file3.read()]
vect=CountVectorizer()
X=vect.fit_transform(doc1).toarray()
X[X>0]=1
df=pd.DataFrame(X,columns=vect.get_feature_names())
print(df)
sum_list=[]
for j in df.index:
    sum1=0
    for i in range(0,len(df.columns)):
        sum1+=df.iloc[j,i]**2
    sum_list.append(sum1)
# print(sum_list)

# for document 1 and document 2
theta=[]
for j in df.index:
    x=0
    for i in range(0,len(df.columns)):
        x+=np.bitwise_and(df.iloc[j,i],df.iloc[(j+1)%3,i])
    x=x/(np.sqrt(sum_list[j])*np.sqrt(sum_list[(j+1)%3]))
    theta.append(x)
    
print(theta)
for i in range(len(theta)):
    if theta[i]>0.5:
        print("document ",i," and ",(i+1)%3," have cosine similarity greater than 0.5")
