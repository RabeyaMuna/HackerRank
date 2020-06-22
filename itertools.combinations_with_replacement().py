from itertools import combinations_with_replacement
s,n=input().split()
l=list(combinations_with_replacement(sorted(s),int(n)))
for i in l:
    print("".join(i))
