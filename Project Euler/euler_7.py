#!/bin/python

import sys
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

t = int(raw_input().strip())
arr=[2]
for a0 in xrange(t):
    n = int(raw_input().strip())
    if len(arr) >= n:
        print arr[n-1]
    else:
        j=len(arr)
        i=arr[j-1]
        if i%2==0:
            i=i+1
        else:
            i=i+2
        while j<n:
            if is_prime(i):
                arr.append(i)
                j=j+1
            i=i+2
        # print arr
        # print j
        print arr[j-1]