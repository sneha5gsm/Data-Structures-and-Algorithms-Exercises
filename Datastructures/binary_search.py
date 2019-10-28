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
        sp.append((s[i], p[i]))
        i = i + 1
    print sp
    sp = sorted(sp, key=lambda x: x[0])
    print sp
    i = 0
    while i < k:
        print '-----'
        print 'i'
        print q[i]
        if q[i] in done.keys():
            ans[i] = done[q[i]]
        else:
            x = n / 2
            j = x
            y = n
            while x >= 1:
                print '====='
                print 'j'
                print j
                print 'x'
                print x
                print 'y'
                print y
                if x == 1:
                    if (j + 1) < n and q[i] >= sp[j + 1][0]:
                        print 'in forst'
                        ans[i] = sp[j + 1][1]
                        done[q[i]] = sp[j + 1][1]
                    elif q[i] >= sp[j][0]:
                        print 'in second'
                        ans[i] = sp[j][1]
                        done[q[i]] = sp[j][1]
                    else:
                        print 'in thirrd'
                        ans[i] = sp[j - 1][1]
                        done[q[i]] = sp[j - 1][1]
                    break
                y = y - x
                x = x / 2
                if q[i] > sp[j][0]:
                    print 'in 1'
                    j = j + x
                elif q[i] < sp[j][0]:
                    print 'in2'
                    j = j - x
                else:
                    print 'inisde elese'
                    ans[i] = sp[j][1]
                    done[q[i]] = sp[j][1]
                    break
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
