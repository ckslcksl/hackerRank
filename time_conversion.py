#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm = s[-2:]
    hour = s[:2]
    if hour == '12' and ampm.upper() == 'AM':
        return str("00")+s[2:-2]
    elif hour == '12' and ampm.upper() == 'PM':
        return s[:-2]
    elif ampm.upper() == 'AM':
        return s[:-2]
    elif ampm.upper() == 'PM':
        return str(int(hour)+12)+s[2:-2]

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()