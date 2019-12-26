#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cumulative_likes = 0
    shared = 5
    for i in range(n):
        todays_likes = math.floor(shared/2)
        cumulative_likes += todays_likes
        shared = todays_likes * 3

    return cumulative_likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
