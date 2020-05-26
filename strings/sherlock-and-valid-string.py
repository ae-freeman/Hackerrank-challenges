#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    # Map string to a dict
    letter_freq = {}

    for char in s:
        if char in letter_freq:
            letter_freq[char] += 1
        else:
            letter_freq[char] = 1

    # Put the values from dict in an array and see how many times they appear
    numbers = []

    for key in letter_freq:
        numbers.append(letter_freq[key])


    number_freq = {}

    for number in numbers:
        if number in number_freq:
            number_freq[number] += 1
        else:
            number_freq[number] = 1
    print(number_freq)


    min_number = min(numbers)
    max_number = max(numbers)


    numbers_range = max_number - min_number


    if numbers_range == 0:
        return "YES"

    if min_number == 1 and number_freq[min_number] == 1:
        numbers.remove(min_number)
        new_range = max(numbers) - min(numbers)
        if new_range == 0:
            return "YES"
        else:
            numbers.append(min_number)

    if numbers_range > 1:
        return "NO"


    elif number_freq[max_number] > 1:
        return "NO"

    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
