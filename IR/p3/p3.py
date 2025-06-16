#AIM:Implement Dynamic programming algorithm for computing the edit distance between 

m=[]
s1=input("enter word1:")
r=len(s1)+1
s2=input("enter word2:")
c=len(s2)+1
if(r==1):
    print("edit distance:",c-1)
elif(c==1):
    print("edit distance:",r-1)
else:
    for i in range(r):
        n=[]
        for j in range(c):
            n.append(0)
        m.append(n)
        
        
    for i in range(r):
        for j in range(c):
            m[i][0]=i
            m[0][j]=j
    for i in range(1,r):
        for j in range(1,c):
            d=m[i-1][j]+1
            e=m[i][j-1]+1
            if(s1[i-1]!=s2[j-1]):
                f=m[i-1][j-1]+1
            else:
                f=m[i-1][j-1]
            m[i][j]=min(d,e,f)
    for i in range(r):            
        print(m[i])
    print("edit distance:",m[r-1][c-1])

    
