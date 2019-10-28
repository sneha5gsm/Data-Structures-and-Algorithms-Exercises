# done
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    k = int(inputFile.readline())
    z = inputFile.readline()
    if k==1:
        fileLine = 'Case #' + str(t + 1) + ": 0" + '\n'
        outputFile.write(fileLine)
    else:
        limit = 0
        if z[len(z)-1] == '\n':
            z = z[: len(z) - 1]
        optimalArray = map(int, z.split(' '))
        print('line')
        print(optimalArray)
        optimalArray = sorted(optimalArray)
        print 'optimal array'
        print optimalArray
        if k%2 == 0:
            limit = k/2 -1
        else:
            limit = (k-3)/2
        print 'linit'
        print limit
        i=0
        sum1 = 0
        sum2 = 0
        diff1 = 0
        j=0
        total = 0
        while i<= limit:
            print 'i'
            print i
            sum1 = sum1 + i*i
            sum2 = sum2 + optimalArray[j]*optimalArray[j]
            diff1 = diff1 + i*optimalArray[j]
            if j%2!=0:
                i=i+1
            j=j+1
        if k%2 !=0:
            sum1 = sum1 + (limit+1)*(limit+1)
            sum2 = sum2 + optimalArray[j]*optimalArray[j]
            diff1 = diff1 + (limit+1)*optimalArray[j]
        total = sum1 + sum2 -2*diff1
        print 'sum1'
        print sum1
        print 'sum2'
        print sum2
        print 'diff1'
        print diff1
        print total
        fileLine = 'Case #' + str(t + 1) + ": " + str(total) + '\n'
        outputFile.write(fileLine)
inputFile.close()
outputFile.close()