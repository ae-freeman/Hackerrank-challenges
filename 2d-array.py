#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #defined constraints, smallest number is -9, hourglass contains 7 numbers, -63 is smallest possible number
    max_sum = -63


    for row in range(4):
        for col in range(4):

            row_1 = arr[row][col] + arr[row][col +1] + arr[row][col + 2]
            row_2 = arr[row + 1][col + 1]
            row_3 = arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]

            hourglass_sum = row_1 + row_2 + row_3

            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
