# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
factorials = {1: 1}


def factorial(n):
    if n in factorials:
        return factorials[n]
    else:
        i = 1
        fact = 1
        while i <= n:
            fact = fact * i
            i = i + 1
        factorials[n] = fact
        return fact


for a0 in xrange(t):
    z = raw_input()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    x = map(int, z.split(' '))
    n = x[0]
    m = x[1]
    # print x
    ans = factorial(n + m) / (factorial(m) * factorial(n))
    ans = ans % 1000000007
    print str(ans)


