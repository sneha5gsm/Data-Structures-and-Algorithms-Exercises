#!/bin/python

import sys
import math

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    maximum=-1
    a=1
    limit =n/2
    while a<limit:
        b1=(n*(n-2*a))/float(2*(n-a))
        b2 = (n*(n-2*a))/(2*(n-a))
        if b1 == b2:
            c =  a*a + b1*b1
            c= c** 0.5
            if c == math.floor(c):
                p = a*b1*c
                if p>maximum:
                    maximum=int(p)
        a=a+1
    print maximum