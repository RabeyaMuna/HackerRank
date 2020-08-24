from itertools import combinations
N=int(input())
B=input().split()
K=int(input())
C=list(combinations(B,K))
D=float(len(C))
ad=0;
for i in C:
    if "a" in i:
        ad+=1
print("{0:.12}".format(ad/D))
