#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.

def cutTheSticks(arr):

    def recursiveFunction(arr):

            #count will initialised at 0 each time
            count = 0

            #check the elements in the array have not already been removed
            if arr:
                min_stick = min(arr)
            else:
                return

            #instead of modifying existing array, create a new one with remaining sticks
            new_sticks = []

            for element in arr:
                count += 1
                new_element = element - min_stick
                if new_element != 0:
                    new_sticks.append(new_element)

            count_array.append(count)

            #call this function again until there are no more sticks in the array
            recursiveFunction(new_sticks)


    count_array = []
    recursiveFunction(arr)

    return count_array





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
