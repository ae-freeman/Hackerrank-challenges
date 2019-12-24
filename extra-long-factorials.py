#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):

    answer = 1
    while(n != 1):
        answer *= n
        n-=1
    print(answer)



if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
