inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    # print line
    n = line[0]
    k=line[1]
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    yogurts = map(int, z.split(' '))
    # print yogurts
    yogurts = sorted(yogurts)
    # print yogurts
    time = 1
    time2 = 0
    i=0
    count =0
    # print 'case##############' + str(t)
    while i< len(yogurts):
        if time2 == k:
            time = time +1
            time2 = 0
        if time <=yogurts[i]:
            count  = count+1
            time2 = time2 +1
        i=i+1
    fileLine = 'Case #' + str(t + 1) + ": " + str(count) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()
