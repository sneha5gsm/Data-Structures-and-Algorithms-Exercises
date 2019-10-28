inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    a = line[0]
    n = line[1]
    p = line[2]
    i=1
    nFactorial = 1
    if a %p == 0 :
        outputFile.write('Case #' + str(t + 1) + ": 0\n")
    else:
        while i<=n:
            nFactorial = nFactorial * 1
            i=i+1
        j = nFactorial
        x = a
        while j>p:
            while x<p:
                x = x+a
            x = x%p
            if x == 1:
                outputFile.write('Case #' + str(t + 1) + ": 1\n")
                break
            if x == 0:
                outputFile.write('Case #' + str(t + 1) + ": 0\n")
                break
            
