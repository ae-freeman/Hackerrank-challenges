#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):

    newList = cost

    # def getSums(myList, target):
    lst = sorted(cost)

    i = 0
    j = len(lst) - 1
    while i <= j:
        tmp = lst[i] + lst[j]


        if tmp > money:

            j -= 1
            continue
        elif tmp < money:

            i += 1
            continue
        else:
            if lst[i] == lst[j]:
                indexOne = newList.index(lst[i]) + 1
                indexTwo = [i for i, n in enumerate(newList) if n == lst[j]][1] + 1
                print(indexOne, indexTwo)
            else:
                indexOne = newList.index(lst[i]) + 1
                indexTwo = newList.index(lst[j]) + 1
                minIndex = min(indexOne, indexTwo)
                maxIndex = max(indexOne, indexTwo)
                print(minIndex, maxIndex)
            return



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
