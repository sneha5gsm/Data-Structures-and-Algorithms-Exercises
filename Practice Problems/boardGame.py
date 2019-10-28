import itertools
def sums(n, firstPlayer):
    i = 0
    firstSums = [0] * n
    while i < 3:
        j = 0
        sum = 0
        while j < n:
            sum = sum + firstPlayer[i * 3 + j]
            j = j + 1
        firstSums[i] = sum
        i = i + 1
    firstSums = sorted(firstSums)
    return firstSums

inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

for t in range(0, testCases):
    n= int(inputFile.readline())
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    secondPlayer = map(int, z.split(' '))
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    firstPlayer = map(int, z.split(' '))
    firstSums = sums(n, firstPlayer)
    # print 'firstsums'
    # print firstSums
    perms = list(itertools.permutations(secondPlayer))
    # print perms
    i=0
    max= 0
    while i<len(perms):
        sum = sums(n,perms[i])
        # print 'sum' + str(i) + '*************'
        # print sum
        j=0
        count = 0
        while j<n:
            if sum[j] > firstSums[j]:
                count  = count +1
            j=j+1
        if count > max:
            max =count
        if count == 2:
            break
        i=i+1
    if max ==2:
        max = 1/float(1)
    else:
        max = max / float(n)
    # print 'max'
    # print max
    fileLine = 'Case #' + str(t + 1) + ": " + str(max) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()
