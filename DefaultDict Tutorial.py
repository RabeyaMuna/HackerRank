from collections import defaultdict
d = defaultdict(list)
list1=[]
n,m=map(int,input().split())
for i in range(n):
    list1=d[input()].append(str(int(i+1)))
for j in range(m):
  print(" ".join(d[input()]) or -1)
