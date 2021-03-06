# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
#
# For example, given the array  we perform the following steps:
#
# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took  swaps to sort the array.
#
# Function Description
#
# Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.
#
# minimumSwaps has the following parameter(s):
#
# arr: an unordered array of integers

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


######### NOTE: both methods failed with really long inputs, they took too long #########
def minimumSwaps(arr):
    swaps = 0

    sorted_array = sorted(arr)

    for i in range(len(arr)):
        if arr == sorted_array:
            break
        elif arr[i] == sorted_array[i]:
            continue
        else:
            correct_value = sorted_array[i]
            swap_with = arr.index(correct_value)
            arr[i], arr[swap_with] = arr[swap_with], arr[i]
            swaps += 1



    return swaps



    swaps = 0
    for i in range (len(arr)):
        if(arr[i]!=(i+1)):
            t=i;
            while(arr[t]!=(i+1)):
                t+=1
            arr[t] = arr[i]
            arr[i] = i + 1

            swaps += 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
