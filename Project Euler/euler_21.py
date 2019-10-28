# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
start = 1
max = 0
inputs = []
done = {}
answers = [0] * t
i = 0
for a0 in xrange(t):
    n = int(raw_input())
    inputs.append((i, n))
    i = i + 1
inputs = sorted(inputs, key=lambda x: x[1])
# print inputs

k = 0
for a0 in xrange(t):
    i = start
    ans = max
    n = inputs[k][1]
    while i < n:
        # print i
        # print 'inside while i'
        if i in done:
            i = i + 1
        else:
            j = 1
            sum1 = 0
            while j < i:
                if i % j == 0:
                    sum1 = sum1 + j
                j = j + 1
            j = 1
            sum2 = 0
            while j < sum1:
                if sum1 % j == 0:
                    sum2 = sum2 + j
                j = j + 1
            if sum2 == i and sum1 != i:
                # print 'if yaya'
                # print i
                # print sum1
                # print sum2
                # print '------'
                done[i] = True
                done[sum1] = True
                ans = ans + i + sum1
            i = i + 1
    answers[inputs[k][0]] = ans
    start = n
    max = ans
    k = k + 1
i = 0
while i < t:
    print answers[i]
    i = i + 1



