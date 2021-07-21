#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    num = n
    for i in range(k):
        arr = []
        mynum = 0
        for j in str(num):
            arr.append(j)

        print(num,mynum,arr)
        for k in range(len(arr)):
            mynum += int(arr[k])
        num = mynum
    return num
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(str(result) + '\n')

