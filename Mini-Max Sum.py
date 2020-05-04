import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min=0
    max=0
    arr.sort()
    
    for i in range (1,len(arr)):
        min+=arr[i-1]
        max+=arr[i]
    print (min,max)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
