#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

    #Initialise variables
    n = len(c)
    i = 0
    energy = 100

    #Jump on each cloud
    while True:
        #Increment one by one to check if have passed by c[0]
        for j in range(k):
            i += 1

        #After increasing by k times, find the corresponding cloud. % n to make it                  circular.
        cloud = c[(i) % n]
        # -1 energy for each move
        energy -= 1
        # -2 energy for each landing on thunderhead
        if cloud == 1:
            energy -= 2

        #Check if i is back to index 0, if it is then finish the loop.
        if i % n == 0:
            break

    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
