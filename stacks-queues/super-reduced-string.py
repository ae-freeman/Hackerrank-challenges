#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):

    sList = list(s)
    stack = []


    for i in range(len(sList)):
        if len(stack) > 0:
            if sList[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(sList[i])

        else:
            stack.append(sList[i])


    if len(stack) == 0:
        return "Empty String"
    else:
        return "".join(stack)










if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
