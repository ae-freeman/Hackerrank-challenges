#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    #Create a dictionary to store each ascii value and corresponding height
    ascii_dict = {}

    #Starting ascii value for lowercase letter
    ascii_value = 97

    #Assign each height in h the corresponding ascii value
    for num in h:
        ascii_dict[ascii_value] = num
        ascii_value += 1

    #Initialise max height
    max_height = 0

    #Find height of each letter in word using its ascii value
    for letter in word:
        height = ascii_dict[ord(letter)]
        if height > max_height:
            max_height = height

    #Return area (height * width)
    return max_height * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
