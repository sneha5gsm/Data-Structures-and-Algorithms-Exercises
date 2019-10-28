#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    i = 999
    maximum = 101101
    # imax=1
    # jmax=1
    while i >= 100:
        j = min(n / i, 999)
        j=max(100,j)
        x=maximum/i
        least = min(999,x)
        least = max(100,least)
        # print '------------'
        # print n/i
        # print j
        # print maximum/i
        # print least
        # print leasstt
        while j >= least:
            # print '---------'
            # print i
            # print j
            # print str(i*j)
            k = str(i * j)
            y = i * j
            if k == k[::-1] and y > maximum and y<n:
                # imax=i
                # jmax=j
                # print '----'
                # print i
                # print j
                maximum = y
            j = j - 1
        i = i - 1
    # print imax
    # print jmax
    print maximum
