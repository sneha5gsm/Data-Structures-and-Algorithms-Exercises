# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
arr = []


def rec(i, j, sum):
    # print '-----'
    if i == (len(arr) - 2):
        # print 'inisde eif'
        # print i
        return max(sum + arr[i + 1][j], sum + arr[i + 1][j + 1])
    else:
        # print 'inside else'
        return max(rec(i + 1, j, sum + arr[i + 1][j]), rec(i + 1, j + 1, sum + arr[i + 1][j + 1]))


for a0 in xrange(t):
    n = int(raw_input())
    # print n
    i = 0
    sum = 0
    arr = []
    while i < n:
        # print i
        # print '--'
        z = raw_input()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        x = map(int, z.split(' '))
        arr.append(x)
        i = i + 1
    if n == 1:
        print arr[0][0]
    else:
        ans = rec(0, 0, arr[0][0])
        print ans
