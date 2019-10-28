import math
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    # print '========'
    params = map(int, inputFile.readline().strip().split(' '))
    n=params[0]
    p=params[1]
    i=0
    arr=[]
    total = int(math.pow(2, n))
    while i < p:
        x=inputFile.readline().strip()
        arr.append(x)
        i=i+1
    arr.sort()
    total = total - int(math.pow(2, n-len(arr[0])))
    i=1
    # print total
    # if t==5:
    #     print arr
    s=arr[0]
    while i<p:
        if arr[i].find(s) !=0:
            s=arr[i]
            total = total - int(math.pow(2, n-len(arr[i])))
            # if t==5:
            #     print 'innn'
            #     print arr[i]
            #     print arr[i-1]
            #     print total
            # print total
        i=i+1
    # print total
    fileLine = 'Case #' + str(t + 1) + ": " + str(total) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()
