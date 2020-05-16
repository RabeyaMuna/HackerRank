import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    p=1
    while n!=1:
        p*=n
        n-=1
    print(p)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
