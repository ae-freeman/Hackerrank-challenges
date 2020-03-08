#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    mag_len = len(magazine)
    note_len = len(note)

    if note_len > mag_len:
        print("No")

    else:

        words = {}
        words_req = {}
        for word in note:
            words[word] = 0
            if word in words_req:
                words_req[word] += 1
            else:
                words_req[word] = 1

        for mag_word in magazine:
            if mag_word in words:
                words[mag_word] += 1


        isEnoughWords = True

        for word in words:
            if words[word] < words_req[word]:
                isEnoughWords = False

        if isEnoughWords:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
