#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    s1_letters = {}
    for letter in s1:
        s1_letters[letter] = 1

    sub_string_exists = False

    for letter in s2:
        if letter in s1_letters:
            sub_string_exists = True
            break

    if sub_string_exists:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
