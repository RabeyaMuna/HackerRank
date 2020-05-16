import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a1 = 0
    b1 = 0
    for i in range(len(apples)):
        temp = a+apples[i]
        if temp>=s and temp<=t:
            a1+=1
    for i in range(len(oranges)):
        temp = b+oranges[i]
        if temp>=s and temp<=t:
            b1+=1
    print (a1)
    print (b1)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
