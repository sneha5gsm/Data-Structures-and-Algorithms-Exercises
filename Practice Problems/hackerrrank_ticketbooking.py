'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
z = raw_input().strip()
z = map(int, z.split(' '))
p=z[0]
s=z[1]
t=z[2]
h=z[3]
x=z[4]
ans  = 0
if s<=t:
    ans = x*h
else:
    y= s-t
    if x <=y:
        ans = p*x
    else:
        ans = p*y + h *(x-y)
print ans