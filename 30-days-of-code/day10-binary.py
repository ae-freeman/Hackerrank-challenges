#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())


    binaryNumber = str(bin(n)[2:])

    current_length = 0
    max_length = 0

    for i in range(len(binaryNumber)):
        if binaryNumber[i] == "1":
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
    max_length = max(current_length, max_length)
    print(max_length)
