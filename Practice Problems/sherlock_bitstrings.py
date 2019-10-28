# done
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n=line[0]
    k=line[1]
    p=line[2]
    # print 'p'
    # print p
    z=p-1
    pBitArray = bin(z)
    pBitArray=pBitArray[2:]
    pBitArray = (n-k-len(pBitArray))*'0' +pBitArray
    pBitArray = map(int, pBitArray)
    # print 'pBitarray'
    # print pBitArray
    bitArray = [None]*n
    i=0
    while i<k:
        i=i+1
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        line = map(int, z.split(' '))
        bitArray[line[0]-1] = line[2]
    # print 'bitArray'
    # print bitArray
    i=0
    j=0
    while i<n:
        if bitArray[i]== None:
            bitArray[i]=pBitArray[j]
            j=j+1
        i=i+1
    # print ''.join(map(str, bitArray))
    fileLine = 'Case #' + str(t + 1) + ": " + ''.join(map(str, bitArray)) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()
