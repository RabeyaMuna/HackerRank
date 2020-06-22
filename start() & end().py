# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n,b=input(),input()
for i in range(len(n)):
    if re.match(b,n[i:]):
       print((i,i+len(b)-1))
if re.search(b,n)==None:
    print((-1, -1))
