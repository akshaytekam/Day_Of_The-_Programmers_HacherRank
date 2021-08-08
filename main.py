#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
 

def dayOfProgrammer(year):
    # Write your code here
    if year < 1918:                                                    # checking the year greater the 1918
        d = 256-244
        return f"{d}.09.{year}"
    elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):      #Checking the Leap year
        d = 256-244
        return f"{d}.09.{year}"
    d1 = 256-243
    return f"{d1}.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
