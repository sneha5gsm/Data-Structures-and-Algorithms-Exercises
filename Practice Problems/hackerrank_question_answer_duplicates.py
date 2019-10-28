'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from fractions import Fraction

# Write your code here
testCases = int(raw_input())
for t in range(0, testCases):
    z = raw_input().strip()
    z = map(int, z.split(' '))
    n = z[0]
    a = z[1]
    b = z[2]
    c = Fraction(a, b)
    a1 = c.numerator
    b1 = c.denominator
    # print a1
    # print b1
    n1 = n + 1
    total = (n1 * (n1 + 1)) / 2
    y = n - (a1 + b1) + 1
    if y > 0:
        x = (y * (y + 1)) / 2
        total = total - x
    print total

