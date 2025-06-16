#Write a program to demonstrate bitwise operation. 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
docs=['why hello there ','omg hello pony','she went there?omg']
vec=CountVectorizer()
x=vec.fit_transform(docs)
print(x)
df=pd.DataFrame(x.toarray(),columns=vec.get_feature_names())
print(df)

w1=input("Enter word1: ")
w2=input("Enter word2: ")
op=input("Enter operator: ")
x=[]
for i in range(df.shape[0]):
    if(op=="&"):
        a=(list(df.loc[:,w1]))[i]&(list(df.loc[:,w2]))[i]
        x.append(a)
    if(op=="|"):
        a=(list(df.loc[:,w1]))[i]|(list(df.loc[:,w2]))[i]
        x.append(a)
    print(x)
for i in range(df.shape[0]):
    if(x[i]==1):
        print("Doc",i)


