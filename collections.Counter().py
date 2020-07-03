# counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

#Sample Code

#>>> from collections import Counter
#>>> 
#>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
#>>> print Counter(myList)
#Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
#print Counter(myList).items()
#[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# print Counter(myList).keys()
#[1, 2, 3, 4, 5]
# print Counter(myList).values()
#[3, 4, 4, 2, 1]

import collections
a=int(input())
income=0
shoes=collections.Counter(map(int,input().split()))
n=int(input())
for i in range (n):
    size, price = map(int,input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print (income)
