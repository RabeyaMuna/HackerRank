n,i=map(int,input().split())
a=[]
for j in range(i):
    a.append(map(float,input().split()))
   
for mark in zip(*a):
    print("{0:.1f}".format(sum(mark)/i))
