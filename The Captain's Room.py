a=int(input())
b=list(map(int,input().split()))
c=set(b)
for i in c:
    b.remove(i)
    if i not in b:
        print(i)
        break
