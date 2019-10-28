inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    n = int(inputFile.readline())
    arr = map(int, inputFile.readline().strip())
    # print arr
    if n%2==0:
        s = n/2
    else:
        s= (n+1)/2
    i=0
    start=0
    while i< s:
        start = start + arr[i]
        i=i+1
    maximum = start
    i=s
    j=0
    while i <n:
        start = start - arr[j] + arr[i]
        i=i+1
        j=j+1
        if start> maximum:
            maximum=start
    fileLine = 'Case #' + str(t + 1) + ": " + str(maximum) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()