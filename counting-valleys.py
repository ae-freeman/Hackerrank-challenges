#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    entered_valley = False
    valleys = 0
    for i in range(n):
        if s[i] == "U":
            level += 1
            print(level)
        else:
            level -= 1
            print(level)

        if level < 0:
            entered_valley = True

        elif level > 0:
            entered_valley = False

        elif level == 0 and entered_valley == True:
            valleys += 1


    return(valleys)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
