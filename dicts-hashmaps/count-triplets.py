#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):

    #initialise dicts and count
    r2 = {}
    r3 = {}
    count = 0

    #loop through array
    for k in arr:
        #if the current value is in the dict for third numbers, then there has been two previous numbers that will satisfy a triplet for this number k, so increase the count for how many times there is a satisfied triplet
        if k in r3:
            count += r3[k]

            #if the current value is in the dict for second numbers, there has been a number before that will satisfy the condition. Need to add value * r to the third numbers dict so it is ready to find new triplets.
        if k in r2:
            #if it is already there, increase it, could be multiple triplets
            if k*r in r3:
                r3[k*r] += r2[k]
            else:
                r3[k*r] = r2[k]
    #Otherwise, it needs to be added to r2 to see if any future numebrs will satisfy the condition.
        if k*r in r2:
            r2[k*r] += 1
        else:
            r2[k*r] = 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
