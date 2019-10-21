# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys


n = input()
wordList = []
for i in range(int(n)):
    word = input()
    wordList.append(word)



for word in wordList:
    evenLetters = []
    oddLetters = []
    for i in range(len(word)):
        if i % 2 == 0:
            evenLetters.append(word[i])
        else:
            oddLetters.append(word[i])

    for letter in evenLetters:
        print(letter, end="")
    print(" ", end="")
    for letter in oddLetters:
        print(letter, end="")

    print()
