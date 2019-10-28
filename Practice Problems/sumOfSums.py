#done small input
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    outputFile.write('Case #' + str(t + 1) + ":\n")
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n = line[0]
    q = line[1]
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    numbers = map(int, z.split(' '))
    i=0
    j=0
    sumsSize = n*(n+1)/2
    # sums = [0]*sumsSize
    sums = []
    cumulativeSums = []
    k=0
    while i<n:
        j=0
        while j<i:
            sums.append(sums[k-i] + numbers[i])
            k=k+1
            j=j+1
        sums.append(numbers[i])
        k=k+1
        i=i+1
        # k=k+1
        # j=i+1
        # while j<n:
        #     sums.append(sums[k-1] + numbers[j])
        #     k=k+1
        #     j=j+1
        # i=i+1
    # print 'sum array'
    # print sums
    sums.sort()
    # print sums
    i=1
    cumulativeSums.append(sums[0])
    while i<sumsSize:
        cumulativeSums.append(cumulativeSums[i-1] + sums[i])
        i=i+1
    # print cumulativeSums
    i=0
    while i< q:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        line = map(int, z.split(' '))
        # print line
        if line[0] == 1:
            outputFile.write(str(cumulativeSums[line[1]-1]) + '\n')
        else:
            outputFile.write(str(cumulativeSums[line[1]-1] - cumulativeSums[line[0]-2]) + '\n')
        # print str(cumulativeSums[line[1]-1] - cumulativeSums[line[0]])
        # outputFile.write(str(cumulativeSums[line[1]] - cumulativeSums[line[0]]) + '\n')
        i = i +1
inputFile.close()
outputFile.close()

