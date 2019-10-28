# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n == 1:
        print '3'
    else:
        x = 1 + (4 * n * n)
        x = x ** (.5)
        x = int((x - 1) / 2)
        y = 1
        i = x
        # print '========'
        while y == 1:
            # print '----'
            # print i
            s = (i * (i + 1)) / 2
            # print s
            # print '--------'
            divisors = 2
            j = 2
            while j < s:
                if s % j == 0:
                    divisors = divisors + 1
                j = j + 1
            if divisors > n:
                print s
                break
            i = i + 1
