#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'computePrices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER_ARRAY p
#  3. INTEGER_ARRAY q
#

def computePrices(n, s, p, q, k):
    i = 0
    done = {}
    ans = [0] * k
    sp = []
    while i < n:
        sp.append((s[i], (p[i], -2)))
        i = i + 1
    print sp
    print q
    i = 0
    while i < k:
        sp.append((q[i], (-1, i)))
        i = i + 1
    sp = sorted(sp, key=lambda x: x[0])
    print sp
    i = 0
    while i < (n + k):
        if sp[i][1][0] == -1:
            j = i - 1
            while sp[j][1][0] == -1:
                j = j - 1
            ans[sp[i][1][1]] = sp[j][1][0]
        i = i + 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    p = map(int, raw_input().rstrip().split())

    k = int(raw_input().strip())

    q = []

    for _ in xrange(k):
        q_item = int(raw_input().strip())
        q.append(q_item)

    res = computePrices(n, s, p, q, k)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
