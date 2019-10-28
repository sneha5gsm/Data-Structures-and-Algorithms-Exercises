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

# t = int(raw_input().strip())
# for a0 in xrange(t):
    # n = long(raw_input().strip())
    # i=0
i=0
while i< 1000000000000:
    if is_prime(i):
        print i
    i=i+1

# !/bin/python

import sys


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        # print '\t',f
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    primes = []
    r = int(n / 2)
    f = 2
    flag = 0
    # print '==================='
    j = 0
    while f <= r:
        # print '---'
        # print f
        # print r
        if n % f == 0:
            flag = 1
            x = n / f
            primes.insert(j, f)
            if x % 2 != 0:
                primes.insert(j + 1, x)
            j = j + 1
        f = f + 1
        r = n / f
        # print '*******'
        # print f
        # print r
    if flag == 0:
        primes.append(n)
    # print primes
    x = len(primes)
    i = x - 1
    while i >= 0:
        if is_prime(primes[i]):
            print primes[i]
            break
        i = i - 1

