from itertools import product
k,m = map(int, input().split())
arr = []
for i in range(k):
	temp = list(map(int, input().split()))
	arr.append(temp[1:])

max1 = 0

for i in list(product(*arr)):
	sum=0
	for j in i:
		sum += pow(j,2)
	sum = sum %m
	if sum > max1:
		max1 = sum
print(max1)
