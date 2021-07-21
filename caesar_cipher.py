#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    k = k% 26       
    result:str = ''
    temp:str = ''
    for i in s:
        temp = chr(ord(i) + k)    
        print(temp , ord(i) , k)    
        if i <= 'Z' and i >= 'A':            
            if temp > 'Z':
                result += chr(ord(temp) - 26)
            else:
                result += temp
        elif i <= 'z' and i >= 'a':
            if temp > 'z':
                result += chr(ord(temp) - 26)
            else:
                result += temp   
        else:
            result += i
            continue                             
    return result 
if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
