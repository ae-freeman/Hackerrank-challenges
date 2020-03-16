#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(Q):
    #
    # initialize the number of bribes
    bribes = 0

    #make the list value the same as the index to make it easier lower down
    Q = [P-1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q):

        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1,0),i):
            if Q[j] > P:
                bribes += 1
    print(bribes)





if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
