# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
terminates = {}
answers = [0] * t
ques = []


def checkTerminates(n):
    if n in terminates.keys():
        return 1
    else:
        while n >= 1:
            if n % 5 == 0:
                n = n / 5
            elif n % 2 == 0:
                n = n / 2
            else:
                break
        if n == 1:
            terminates[n] = 1
            return 1
        else:
            return n


i = 0
print checkTerminates(4)
print str(1 / float(1969))
for a0 in xrange(t):
    n = int(raw_input().strip())
    ques.append((i, n))
    i = i + 1
ques = sorted(ques, key=lambda x: x[1])
i = 0
start = 4
max = 0
while i < t:
    n = ques[i][1]
    j = start
    while j < n:
        if checkTerminates(j) != 1:
            print '------------'
            print j
            checkstring = ''
            k = 10
            flag = 0
            while True:
                if k < j:
                    k = k * 10
                    checkstring = checkstring + '0'
                    added = s
                else:
                    added = str(k / j)
                    checkstring = checkstring + added
                    k = k % j
                if checkstart != -1:
                    if added == checkstring[checkstart]:
                        count = count + 1
                else:
                    if checkstring(len(checkstring) - 1) == checkstring[0]:
                        checkstart = 1
                        count = 1

            count = 0
            x = 1 / float(j)
            count = count + 1
            print x
            if count > max:
                max = count
        j = j + 1
    answers[ques[i][0]] = max
    start = n
    i = i + 1
i = 0
print '===='
print str(1 / float(1969))

while i < t:
    print answers[i]
    i = i + 1

