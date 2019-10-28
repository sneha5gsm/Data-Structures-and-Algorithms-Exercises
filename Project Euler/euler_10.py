#!/bin/python

import sys

primes={2:True, 3:True}
def is_prime(n):
    if n in primes:
        return True
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
    primes[n]=True
    return True

arr ={1:0, 2:2}
t = int(raw_input().strip())
for a0 in xrange(t):
    # print '============='
    n = int(raw_input().strip())
    if n in arr:
        print str(arr[n])
    else:
        if n%2==0:
            i=n-1
        else:
            i=n
        sum=0
        y = -1
        flag=0
        while i>2:
            if is_prime(i):
                # print '----'
                # print i
                if y== -1:
                    y=i
                if i in arr:
                    flag =1
                    sum= sum+ arr[i]
                    break
                else:
                    # print 'inside else'
                    sum= sum+ i
                    # print sum
            i=i-2
        if flag==0:
            sum= sum+2
        if y!= -1:
            arr[y] = sum
        # print arr
        print str(sum)    