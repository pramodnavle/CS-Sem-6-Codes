#Aim : Write a map-reduce program to count the number of occurrences of each alphabetic character in the given dataset. 
#The count for each letter should be case-insensitive (i.e., include both upper-case and lower-case versions of the letter; Ignore non-alphabetic characters).


from collections import Counter

# initializing string

test =input("Enter a String : ")

#using collections.Counter() to get

#count of each element in string
res = Counter(test.casefold())

#printing result

print ("Output " + str(res))
