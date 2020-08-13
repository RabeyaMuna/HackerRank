n,n1=input().split()
n2=list(map(int, input().split()))[:int(n)]
A=set(map(int,input().split()))
B=set(map(int,input().split()))
count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in n2]
print(sum(count))
