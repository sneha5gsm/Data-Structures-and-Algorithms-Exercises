# done
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    k = int(inputFile.readline())
    # print len(bin(k)[2:])
    binary = bin(k)[2:]
    logTwo = len(binary)
    if binary.count('1') == 1:
        fileLine = 'Case #' + str(t + 1) + ": " + '0' + '\n'
        outputFile.write(fileLine)
    else:
        output = '0'
        x = pow(2, logTwo)
        while k>0:
            y = x/2
            if k == y:
                break
            if k > y:
                output = '1'
                k = k - y
            else:
                output = '0'
            x = y
        fileLine = 'Case #' + str(t + 1) + ": " + output + '\n'
        outputFile.write(fileLine)
inputFile.close()
outputFile.close()