#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    mins = [sys.maxsize, sys.maxsize]

    for i, p in reversed(list(enumerate(q, 1))):

        if p - i > 2:
            print('Too chaotic')
            return
        elif p > mins[1]:
            bribes += 2
        elif p > mins[0]:

            bribes += 1


        if p < mins[0]:

            mins = (p, mins[0])

        elif p < mins[1]:

            mins = (mins[0], p)
    print(bribes)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
