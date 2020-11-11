n=int(input())
for i in range(0,n):
    n1=int(input())
    a=list(map(int,input().split()))[:n1]
    if a[0]==max(a) or a[n1-1]==max(a):
        print("Yes")
    else:
        print("No")
