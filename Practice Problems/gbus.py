inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    n = int(inputFile.readline())
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    i=0
    gbusTupleArray = []
    while i<len(line):
        gbusTupleArray.append((line[i], line[i+1]))
        i=i+2
    gbusTupleArray = sorted(gbusTupleArray, key=lambda k: k[0])
    # print 'gbusTupleArray'
    # print gbusTupleArray
    # gbusTupleArray = sorted(gbusTupleArray, key=lambda k: k[1])
    # print gbusTupleArray
    p = int(inputFile.readline())
    parray = []
    i=0
    while i< p:
        parray.append((int(inputFile.readline()), i))
        i=i+1
    parray.sort()
    parrayResult = [0] *len(parray)
    inputFile.readline()
    i=0
    while i< len(gbusTupleArray):
        j=0
        if len(parray) == 0:
            break
        while j<len(parray):
            # print 'i,j'
            # print i,j
            if gbusTupleArray[i][0] <= parray[j][0] and gbusTupleArray[i][1] >= parray[j][0]:
                parrayResult[parray[j][1]] = parrayResult[parray[j][1]] + 1
                # print parrayResult
            if gbusTupleArray[i][1] < parray[j][0]:
                break
            if gbusTupleArray[i][0] > parray[j][0]:
                # print 'iniside pop'
                # print gbusTupleArray[i][0]
                # print  parray[j]
                # parrayResult[parray[j][1]] = parrayResult[parray[j][1]]
                parray.pop(j)
                j=j-1
                # print parray
            j=j+1
        i=i+1
    fileLine = 'Case #' + str(t + 1) + ": " + ' '.join(str(x) for x in parrayResult) + '\n'
    outputFile.write(fileLine)
    # print 'result array'
    # print parrayResult
inputFile.close()
outputFile.close()