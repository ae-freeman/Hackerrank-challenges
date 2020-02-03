# A modified Kaprekar number is a positive whole number with a special property.
# If you square it, then split the number into two integers and sum those integers,
# you have the same value you started with.

# Given two positive integers p and  q where p is lower than q, write a program to print
# the modified Kaprekar numbers in the range between p and q, inclusive.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):

    k_numbers = []

    for i in range(p, q + 1): #make the range inclusive
        squared = str(int(math.pow(i, 2)))
        length = len(squared)

        #slice string in half, right side is bigger and == length
        first_half = squared[:math.floor(length/2)]
        second_half = squared[math.floor(length/2):]

        #prepare to check for single digit squares
        second_half_int = int(second_half)

        if not first_half and second_half_int == i:
            k_numbers.append(i)

        #check rest of the numbers
        if(first_half):
            first_half_int = int(first_half)

            total = first_half_int + second_half_int

            if total == i:
                k_numbers.append(i)

    if len(k_numbers) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(x) for x in k_numbers))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
