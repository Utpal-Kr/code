# https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n % 2 == 0):
    if (n < 6):
        print ('Not Weird')
    if (n > 5 ):
        if (n<21):
          print ('Weird')
    if(n>20) :
        print ('Not Weird')
else:
    print('Weird')