# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    name,space,price=input().rpartition(' ')
    d[name]=d.get(name,0)+int(price)
for name,price in d.items():
    print(name,price )
