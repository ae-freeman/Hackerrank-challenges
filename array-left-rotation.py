#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))


    starting_point = d % n
    new_list = []

    for i in range(n):
        new_list.append((a[(starting_point + i) % n]))

    print(*new_list)
