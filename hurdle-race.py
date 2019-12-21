#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    #find max value in height
    max_hurdle = max(height)

    #check if initial jump height k is less than max height
    if k < max_hurdle:
        #find difference between height and k, the initial height he can jump
        num_doses = max_hurdle - k
        return num_doses

    else:
        return 0




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
