string,k=input().split()
from itertools import permutations
l=list(permutations(sorted(string),int(k)))
for i in l:
    print("".join(i))
