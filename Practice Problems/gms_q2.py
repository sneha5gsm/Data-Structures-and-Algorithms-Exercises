#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def solve(p, n):
    total = 0
    i = 0
    n = n + 1
    p.insert(0, 0)
    sums1 = [0] * (n)
    sums2 = [0] * (n)
    sums1[0] = 0
    sums2[n - 1] = 0
    while i < (n - 1):
        if (p[i] - p[i + 1]) > 0:
            total = total + p[i] - p[i + 1]
        else:
            total = total + p[i + 1] - p[i]
        sums1[i + 1] = total
        i = i + 1
    i = n - 1
    total2 = 0
    while i > 0:
        if (p[i] - p[i - 1]) > 0:
            total2 = total2 + p[i] - p[i - 1]
        else:
            total2 = total2 + p[i - 1] - p[i]
        sums2[i - 1] = total2
        i = i - 1
    # print sums1
    # print sums2
    i = 1
    minimum = total
    # print minimum
    # print '===='
    while i < (n - 1):
        j = i + 1
        while j < n:
            tempsum = 0
            x1 = 0
            x2 = 0
            y2 = 0
            y1 = 0
            if i > 0:
                if p[j] - p[i - 1] > 0:
                    x1 = p[j] - p[i - 1]
                else:
                    x1 = p[i - 1] - p[j]
                x1 = x1 + sums1[i - 1]
            if p[j] - p[i + 1] > 0:
                x2 = p[j] - p[i + 1]
            else:
                x2 = p[i + 1] - p[j]
            if p[i] - p[j - 1] > 0:
                y1 = p[i] - p[j - 1]
            else:
                y1 = p[j - 1] - p[i]
            if j < (n - 1):
                if p[i] - p[j + 1] > 0:
                    y2 = p[i] - p[j + 1]
                else:
                    y2 = p[j + 1] - p[i]
                y2 = y2 + sums2[j + 1]
            if j == (i + 1):
                # print 'inside 8888'
                # print tempsum
                if p[i] - p[j] > 0:
                    tempsum = x1 + p[i] - p[j] + y2
                else:
                    tempsum = x1 + p[j] - p[i] + y2
                # print tempsum
            else:
                tempsum = sums1[j - 1] - sums1[i + 1] + x1 + x2 + y1 + y2
            # print '----------'
            # print i
            # print j
            # print x1
            # print x2
            # print y1
            # print y2
            # print tempsum
            if tempsum < minimum:
                minimum = tempsum
            j = j + 1
        i = i + 1
    return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p_count = int(raw_input().strip())

    p = map(int, raw_input().rstrip().split())

    result = solve(p, p_count)

    fptr.write(str(result) + '\n')

    fptr.close()
