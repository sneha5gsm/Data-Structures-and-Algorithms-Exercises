inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

def merge(s1,s2, n1, n2):
    i = 0
    j = 0
    s=''
    while (i < n1 and j < n2):
        if int(s1[i]) <= int(s2[j]):
            s=s+ s1[i] + '*'
            i =i+1
        else:
            s = s + s2[j] + '*'
            j = j + 1
    while i<n1:
        s=s+s1[i] + '*'
        i=i+1
    while j<n2:
        s=s+s2[j] + '*'
        j=j+1
    # print 'in fn'
    # print s1
    # print s2
    # print s
    return s
for t in range(0, testCases):
    z = inputFile.readline().strip()
    # if z[len(z) - 1] == '\n':
    #     z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n=line[0]
    q=line[1]
    l=[0]*n
    r=[0]*n
    classes = [0]*n
    z = inputFile.readline().strip()
    # if z[len(z) - 1] == '\n':
    #     z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    x1 = line[0]
    x2 = line[1]
    a1 =line[2]
    b1 =line[3]
    c1=line[4]
    m1=line[5]
    z = inputFile.readline().strip()
    # if z[len(z) - 1] == '\n':
    #     z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    y1 = line[0]
    y2 = line[1]
    a2 = line[2]
    b2 = line[3]
    c2 = line[4]
    m2 = line[5]
    z = inputFile.readline().strip()
    # if z[len(z) - 1] == '\n':
    #     z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    z1 = line[0]
    z2 = line[1]
    a3 = line[2]
    b3 = line[3]
    c3 = line[4]
    m3 = line[5]
    i=2
    # print '==========='
    if n>0:
        if x1 > y1:
            l[0] = y1 + 1
            r[0] = x1 + 1
        else:
            l[0] = x1 + 1
            r[0] = y1 + 1
        j=l[0]
        s=''
        while j<=r[0]:
            s=s+str(j)
            j=j+1
        classes[0] = (s, r[0]-l[0]+1)
    if n>1:
        if x2 > y2:
            l[1] = y2 + 1
            r[1] = x2 + 1
        else:
            l[1] = x2 + 1
            r[1] = y2 + 1
        j = l[1]
        s = ''
        while j <= r[1]:
            if
            j = j + 1
        classes[1] = (s, r[1] - l[1] + 1)
    while i<n:
        x3= (a1*x2 + b1*x1 + c1)% m1
        y3=(a2*y2 + b2*y1 + c2)%m2
        # print x3
        # print y3
        if x3>y3:
            l[i] = y3 +1
            r[i]  = x3+1
        else:
            l[i] = x3+1
            r[i] = y3+1
        j = l[i]
        s = ''
        while j <= r[i]:
            s = s + str(j)
            j = j + 1
        classes[i] = (s, r[i] - l[i] + 1)
        x1=x2
        y1=y2
        x2=x3
        y2=y3
        i=i+1
    if n>1:
        x=merge(classes[0][0],classes[1][0], classes[0][1], classes[1][1])
        # print x
        i=2
        while i<n:
            # print '----'
            # print x
            # print classes[i]
            x=merge(x, classes[i][0],len(x), classes[i][1])
            i=i+1
        # print x
    else:
        x=classes[0][0]
    # print x
    sum=0
    total=len(x)
    k=z1+1
    # print total
    # print k
    # print s[total-k]
    if k<=total:
        sum= int(x[total-k])
        # print '-----'
        # print sum
    if q>1:
        k = z2 + 1
        if k <= total:
            sum = sum + int(x[total - k])*2
            # print '-----'
            # print sum
    i=2
    while i<q:
        z3= (a3*z2 + b3*z1 + c3)% m3
        k=z3+1
        if k <= total:
            sum = sum + int(x[total - k])*(i+1)
            # print '-----'
            # print sum
        z1=z2
        z2=z3
        i=i+1
    fileLine = 'Case #' + str(t + 1) + ": " + str(sum) + '\n'
    outputFile.write(fileLine)


