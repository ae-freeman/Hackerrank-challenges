#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    pattern = r'@gmail\.com$'

    firstNamesList = []

    regex = re.compile(pattern)


    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if regex.search(emailID):

            firstNamesList.append(firstName)


    firstNamesList.sort() #automatically sorts it alphabetically

    for name in firstNamesList:
        print(name)
