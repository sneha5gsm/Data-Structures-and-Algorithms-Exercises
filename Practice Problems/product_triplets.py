inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    n=int(inputFile.readline())
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    line = sorted(line)
    # print line
    count =0
    # total =0
    i=0
    # print '======'
    while i<n-2:
        j=i+1
        while j<n-1:
            k=j+1
            while k<n:
                # total=total +1
                if line[i] == 0 and line[j]==0:
                    count=count+1
                elif line[i]*line[j] == line[k]:
                    # print 'inisde'
                    # print z
                    # print line[i]
                    # print line[j]
                    # print line[k]
                    count = count+1
                k=k+1
            j=j+1
        i=i+1
    # print total
    fileLine = 'Case #' + str(t + 1) + ": " + str(count) + '\n'
    outputFile.write(fileLine)