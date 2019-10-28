'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here
def recursiveFn(n, total, probTillNow, three, two, arr):
    if n in arr:
        total = total + arr[n]
    elif n < 2:
        # print 'inside eless than 2'
        # print n
        # print 'total'
        # print total
        # print 'probtilnow'
        # print probTillNow
        return total
    elif n == 2:
        # print 'inside if 2'
        # print n
        # print 'total'
        # print total
        # print 'probtilnow'
        # print probTillNow
        total = total + probTillNow * two
        return total
    elif n == 3:
        # print 'inside if 3'
        # print n
        # print 'total'
        # print total
        # print 'probtilnow'
        # print probTillNow
        total = total + probTillNow * three
        return total
    else:
        # print 'inside else n'
        # print n
        # print 'total'
        # print total
        # print 'probtilnow'
        # print probTillNow
        arr[n - 2] = recursiveFn(n - 2, total, probTillNow * two, three, two, arr)
        arr[n - 3] = recursiveFn(n - 3, total, probTillNow * three, three, two, arr)
        total = total + arr[n - 2] + arr[n - 3]
        return total


z = raw_input()
if z[len(z) - 1] == '\n':
    z = z[: len(z) - 1]
line = map(int, z.split(' '))
n = line[0]
p = line[1]
# print p
two = p / float(100)
three = 100 - p
three = three / float(100)
arr = {}
# print 'three'
# print three
# print 'two'
# print two
print '%.6f' % recursiveFn(n, 0, 1, three, two, arr)

