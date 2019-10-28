inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
import math
testCases = int(inputFile.readline())
done1={}
import operator as op
factorials = {1: 1}
d = 1000000007

# def ncr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, xrange(n, n-r, -1), 1)
#     denom = reduce(op.mul, xrange(1, r+1), 1)
#     return numer//denom
def modFact(n, p):
    if n in factorials:
        return factorials[n]
    else:
        if n >= p:
            return 0
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % p
        factorials[n] = result
        return result

# def ncr(n,r):
#     x = modFact(n,d)/(modFact(n-r,d)*modFact(r,d))
#     return x
# Python3 function to
# calculate nCr % p
def ncr(n, r, p):
    # initialize numerator
    # and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


# p must be a prime
# greater than n
# def factorial(n):
#     if n in factorials:
#         return factorials[n]
#     else:
#         i = 1
#         fact = 1
#         while i <= n:
#             fact = fact * i
#             i = i + 1
#         factorials[n] = fact
#         return fact

def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n in factorials:
        return factorials[n]
    else:
        if n < 2:
            return 1
        return range_prod(1,n)

for t in range(0, testCases):
    arr = map(int, inputFile.readline().strip().split(' '))
    n=arr[0] *2
    m=arr[1]
    print '---------'
    # print n
    # print m
    i=1
    total = modFact(n,d)
    # print total
    while i<=m:
        # print '===='
        if i%2!=0:
            total = total - (ncr(m,i,d) * modFact(n -i,d))*int(pow(2,i,d))
        else:
            total =total  + ncr(m,i,d) * modFact(n -i,d)*int(pow(2,i,d))
        total = total % 1000000007
        # print total
        i=i+1
    print total
    fileLine = 'Case #' + str(t + 1) + ": " + str(total) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()


