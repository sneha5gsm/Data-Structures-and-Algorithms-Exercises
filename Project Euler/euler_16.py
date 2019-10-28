# Enter your code here. Read input from STDIN. Print output to STDOUT
def f(x):
    return {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0,
    }[x]


t = int(raw_input())
for a0 in xrange(t):
    n = int(raw_input().strip())
    x = str(int(2 ** n))
    sum = 0
    i = 0
    l = len(x)
    while i < l:
        sum = sum + f(x[i])
        i = i + 1
    print str(sum)
