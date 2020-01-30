#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):

    page_counter = 1
    special_numbers = 0

    for chapter in range(n):
        problem_counter = 0
        for problem in range(arr[chapter]):
            if (problem + 1) == page_counter:
                special_numbers += 1

            problem_counter += 1
            if problem_counter == k:
                problem_counter = 0
                page_counter += 1


        check_new_page = arr[chapter] / k

        if (check_new_page % 1 != 0):
            page_counter += 1

    return special_numbers



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
