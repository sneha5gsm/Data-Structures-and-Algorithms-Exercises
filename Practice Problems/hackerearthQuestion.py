'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
testCases=int(raw_input())
for t in range(0, testCases):
    z = raw_input()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n=line[0]
    k=line[1]
    i=0
    arrays = [0]*k
    while i<k:
        z = raw_input()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        arrays[i] = map(int, z.split(' '))
        i=i+1
    # print 'arrays'
    # print arrays
    i=0
    minimum = 1000000001
    minimumLength = n
    maximum = -1
    maximumLength = 0
    while i< (1<<n):
        j=0
        length = 0
        q=1
        while j<n:
            if i&(1<<j):
                length = length +1
                k=0
                sum=0
                while k<n:
                    # print 'k'
                    # print k
                    # print j
                    sum=sum+arrays[k][j]
                    k=k+1
                q=q*sum
                # sum=0
            j=j+1
        if length!=0:
            q=q/length
            q=q%(1000000007)
            if q>maximum:
                maximum=q
                maxLength = length
            if q<minimum:
                minimum = q
                minLength = length
        q=1
        length = 0
        i=i+1
    print str(maximum^minimum) + ' ' + str(maxLength^minLength)