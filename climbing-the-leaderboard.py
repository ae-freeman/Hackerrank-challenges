#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):

    scores_set = sorted(set(scores))
    counter = 0
    n = len(scores_set)
    alice_positions = []

    for i in alice:
        while (n > counter and i >= scores_set[counter]):
            counter += 1
        alice_positions.append(n + 1 - counter)

    return alice_positions



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
