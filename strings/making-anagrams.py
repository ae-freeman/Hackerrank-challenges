#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    deletions = 0

    # Create dictionaries to track the frequency of each letter
    a_dict = {}
    b_dict = {}

    for char in a:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1

    for char in b:
        if char in b_dict:
            b_dict[char] += 1
        else:
            b_dict[char] = 1
    print(a_dict, b_dict)

    #loop over one string, if that doesn't exist in the other string, delete it
    for char in a:
        if char not in b:
            deletions += 1
        # Case that letter exists, but has already been used by an earlier letter
        elif char in b and b_dict[char] == 0:
            deletions += 1
        else:
            b_dict[char] -= 1


    for char in b:
        if char not in a:
            deletions += 1
        elif char in a and a_dict[char] == 0:
            deletions += 1
        else:
            a_dict[char] -= 1



    return deletions





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
