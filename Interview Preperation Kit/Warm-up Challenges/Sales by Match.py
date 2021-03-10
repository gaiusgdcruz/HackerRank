#Sales by Match

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    #ic = 0
    #jc = 0
    for i in range(0,len(ar)):
        if ar[i] != 0:
            for j in range(i+1,len(ar)):
                #if ar[j]>1:
                    #ar.pop(i)
                if ar[i] == ar[j]:
                    count += 1
                    ar[j] = 0
                    break
                    #ar.pop(j)
                    #ar.pop(i)
    return count   
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


