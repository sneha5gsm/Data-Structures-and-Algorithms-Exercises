# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
fibs = [1, 1]
answers = {1: 1}


def fib(n):
    try:
        # print 'inside try'
        # print fibs
        return fibs[n]
    except:
        x = fib(n - 1) + fib(n - 2)
        fibs.append(x)
        # print fibs
        return x


for a0 in xrange(t):
    n = int(raw_input().strip())
    ten = 10 ** (n - 1)
    if n in answers:
        print answers[n]
    else:
        j = n - 1
        z = len(answers)
        # print answers.keys()
        i = 2
        k = 0
        while k < z:
            if j in answers.keys():
                i = answers[j] + 1
                break
            else:
                j = j - 1
                k = k + 1
        while True:
            # print i
            if fib(i) / ten > 0:
                print str(i + 1)
                answers[n] = i + 1
                break
            i = i + 1


