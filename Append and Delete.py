import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    a=list(s)
    b=list(t)
    c=0
    if s==t:
        c=len(a)+len(b)+1
    if s!=t:
        j=0
        for i in range (0,min(len(a),len(b))):
            if a[i]!=b[i]:
                break
            j+=1
        nonmatch1=len(a)-j
        nonmatch2=len(b)-j
        c= nonmatch1+nonmatch2

    

    if k==c:
        return "Yes"
    return "No"




    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
