#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #

    if n == p:
        return 0

    if p % 2 == 0:
        front = int(p/2)

    else:
        front = int(math.floor(p/2))

    if n % 2 == 0:
        back = int(math.ceil((n - p)/2))
    elif p % 2 == 0:
        back = int((math.ceil((n - p)/2)) - 1)
    else:
        back = int((math.ceil((n - p)/2)))

    result = min(front, back)

    return result




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
