a=[]
for _ in range(int(input())):
    a.append(input())
c=0
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(len(d))
print(*d.values())
