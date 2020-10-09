import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
        key=arr[n-1]
        j=n-2
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            print(*arr)
        arr[j+1]=key
        print(*arr)
        
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
