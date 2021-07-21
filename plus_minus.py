#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr_l = len(arr)
    num_p = 0
    num_m = 0
    num_z = 0

    for num in arr:
        if(num > 0) :
            num_p += 1
        elif(num < 0 ):
            num_m += 1
        elif(num == 0 ):
            num_z += 1
    
    print("{0:.6f}".format(num_p/arr_l))
    print("{0:.6f}".format(num_m/arr_l))
    print("{0:.6f}".format(num_z/arr_l))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)