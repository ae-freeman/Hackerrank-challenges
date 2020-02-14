#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    counter = 0
    moves = 0
    isEmptyString = False

    len_s = len(s)
    len_t = len(t)

    while s[counter] == t[counter]:
        counter += 1
        if counter == len_s or counter == len_t:
            break

    # Case if strings are exactly equal
    if counter == len_s and len_t * 2 <= k:
       return "Yes"


   # Find remaining letters not equal to t string
    toDelete = len_s - counter
    print("toDelete: ", toDelete)

    if toDelete > k:
        return "No"

    moves += toDelete

    # If remaining moves, check if can delete and add on letters in t
    if ((len_t * 2) <= (k - moves)):
        return "Yes"

    # If all letters in s end up deleted, isEmptyString = True so that extra moves can
    # be used deleting from empty string if needed
    if moves == len(s):
        isEmptyString = True

    # Remaining letters in t string to add to moves
    moves += len_t - counter

    if (k - moves) % 2 == 0 and (k - moves) > 0:
        return "Yes"

    elif moves == k:
        return "Yes"

    elif moves < k and isEmptyString == True:
        return "Yes"

    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
