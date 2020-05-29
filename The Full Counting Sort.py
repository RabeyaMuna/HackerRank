#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    ans=" "
    a=[[] for i in range(len(arr))]
    for i in range(len(arr)):
        if i<len(arr)//2:
            arr[i][1]="-"
    for i in range(len(arr)):
        a[int(arr[i][0])].append(arr[i][1])
    
    for d in a:
        for c in d:
            print(c+" ",end="")
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
