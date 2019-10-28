# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
done = {1: [1, 1]}
maximum = 1
for a0 in xrange(t):
    n = int(raw_input())
    if n in done.keys():
        print done[n][1]
    else:
        i = maximum
        # print '-----'
        # print maximum
        while True:
            if i <= n:
                # print 'inside'
                # print i
                break
            i = i - 2
        # print rows
        # print total
        start = done[i][0]
        rows = i
        total = done[i][1]
        while rows < n:
            total = total + start * 4 + 10 * (rows + 1)
            start = start + 4 * (rows + 1)
            rows = rows + 2
            done[rows] = [start, total % 1000000007]
            maximum = rows
        # print done
        print total % 1000000007

