#!/bin/python

import math
import os
import random
import re
import sys


# Complete the nonDivisibleSubset function below.
def recursiveFn(arr, sub, k, count, index):
    if index >= len(arr):
        return count
    else:
        i = 0
        count1 = 0
        count2 = 0
        count3 = 0
        flag = 0
        # print sub
        # print count
        # print 'sub'
        # print len(sub)
        while i < len(sub):
            # print i
            # print index
            # print '--------'
            if (sub[i] + arr[index]) % k == 0:
                flag = 1
                # print 'inside if'
                count1 = recursiveFn(arr, sub, k, count, index + 1)
                count2 = recursiveFn(arr, sub[:i] + sub[i + 1:] + [arr[index]], k, count, index + 1)
            i = i + 1
        if flag == 0:
            count3 = recursiveFn(arr, sub + [arr[index]], k, count + 1, index + 1)
        count = max(count1, count3, count2)
        return count


def nonDivisibleSubset(k, S):
    count = recursiveFn(S, [], k, 0, 0)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = map(int, raw_input().rstrip().split())

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()