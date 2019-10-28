inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n = line[0]
    k=line[1]
    i=0
    p1 = [0]*6
    p2 = [0]*6
    a1=[0]*6
    b1=[0]*6
    c1=[0]*6
    m1=[0]*6
    while i<4:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        line = map(int, z.split(' '))
        p1[i] = line[0]
        p2[i]=line[1]
        a1[i] = line[2]
        b1[i] = line[3]
        c1[i]=line[4]
        m1[i] = line[5]
        i=i+1
    i=2
    p=[0]*n
    p[0] = p1[0]
    p[1] = p2[0]
    h=[0]*n
    h[0] = p1[1]
    h[1] = p2[1]
    x=[0]*k
    x[0] = p1[2]
    x[1] = p2[2]
    y=[0]*k
    y[0] = p1[3]
    y[1] = p2[3]
    while i<n:
        p[i] = (a1[0] * p[i-1] +b1[0]*p[i-2] +c1[0])%m1[0] +1
        h[i] = (a1[1] * h[i - 1] + b1[1] * h[i - 2] + c1[1]) % m1[1] + 1
        i=i+1
    i=2
    while i<k:
        x[i] = (a1[2] * x[i-1] +b1[2]*x[i-2] +c1[2])%m1[2] +1
        y[i] = (a1[3] * y[i - 1] + b1[3] * y[i - 2] + c1[3]) % m1[3] + 1
        i=i+1
    # print p
    # print h
    # print x
    # print y
    i=0
    balloon = 0
    while i<k:
        j=0
        while j<n:
            if x[i] == p[j] and y[i]<=h[j]:
                balloon = balloon + 1
                break
            diff = x[i]-p[j]
            if diff <0:
                diff = p[j] - x[i]
            if h[j] >= y[i] + diff:
                balloon = balloon +1
                break
            else:
                j=j+1
        i=i+1
    outputFile.write('Case #' + str(t + 1) + ": " + str(balloon) + '\n')
inputFile.close()
outputFile.close()


