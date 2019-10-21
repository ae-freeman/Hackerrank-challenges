#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesOnHouse = 0
    for i in range(int(m)):
        if a + apples[i] >= s and a + (apples[i]) <= t:
            applesOnHouse += 1


    orangesOnHouse = 0
    for i in range(int(n)):
        if b + (oranges[i]) >= s and b + (oranges[i]) <= t:
            orangesOnHouse += 1

    print(applesOnHouse)
    print(orangesOnHouse)




if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
