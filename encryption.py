#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    length = len(s)
    square_root = math.sqrt(length)

    rows = math.floor(square_root)
    columns = math.ceil(square_root)

    if rows * columns < length:
        rows = columns

    encrypted_list = ""

    for i in range(0, columns):
        encrypted_list += s[i : length : columns] + " "

    return(encrypted_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
