#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):

    #initialise beautiful day counter
    number_beautiful_days = 0

    for num in range(i, j + 1):

        #reverse number
        reversedNumber = str(num)[::-1]

        #find difference between original number and reversed number
        difference = int(num) - int(reversedNumber)

        #divide difference by k, check if remainder is 0
        if difference % k == 0:
            number_beautiful_days += 1

    return(number_beautiful_days)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
