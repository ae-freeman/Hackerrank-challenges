#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    timeOfDay = str((s[8]))
    if timeOfDay == "P":
        firstTwoChars = int((s[:2])) + 12
        if firstTwoChars == 24:
            firstTwoChars -= 12
        return(str(firstTwoChars) + s[2:8])

    elif int(s[:2]) == 12:
        firstTwoChars = int((s[:2])) - 12
        return("0" + str(firstTwoChars) + s[2:8])


    return(s[0:8])




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
