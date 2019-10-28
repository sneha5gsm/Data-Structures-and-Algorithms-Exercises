inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

for t in range(0, testCases):
    l = int(inputFile.readline())
    a = inputFile.readline()
    if a[len(a) - 1] == '\n':
        a = a[: len(a) - 1]
    b = inputFile.readline()
    if b[len(b) - 1] == '\n':
        b = b[: len(b) - 1]
    i=0
    n=len(a)
    i=1
    adic = {}
    bdic = {}
    while i<=n:
        adic[i] = []
        bdic[i] = []
        i=i+1
    i=0
    while i<n:
        j=i
        total1 = 0
        total2=0
        while j<n:
            if a[j]=='B':
                total1 = total1 +1
            x=j-i+1
            adic[x].append(total1)
            if b[j]=='B':
                total2 = total2 +1
            x=j-i+1
            bdic[x].append(total2)
            j=j+1
        i=i+1
    i=1
    count =0
    # print adic
    # print bdic
    while i<=n:
       j=0
       while j< len(adic[i]):
           try :
                p=bdic[i].index(adic[i][j])
                count = count+1
           except:
               count = count
           j=j+1
       i=i+1
    fileLine = 'Case #' + str(t + 1) + ": " + str(count) + '\n'
    outputFile.write(fileLine)
