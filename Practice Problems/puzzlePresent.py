inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
def fn(matrix, r,c):
    i = 0
    while i < r:
        j = 0
        while j < c:
            k = 0
            while k < w:
                if matrix[i][j] == words[k]:
                    match = match + 1
                k = k + 1
            j = j + 1
        i = i + 1
    funValue = match / (r + c)
    return funValue
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    r = line[0]
    c= line[1]
    w=line[2]
    i=0
    matrix = []
    words=[]
    while i<r:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        matrix.append(list(z))
        i=i+1
    i=0
    while i<w:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        words.append(z)
        i=i+1
    # print matrix
    # print words
    funValues = []
    i=1
    while i<=r:
        j=1
        while j<=c:
            funValues.append(fn(matrix, r,c))
            j=j+1
        i=i+1
    funValues.sort(reversed)
    print funValues
    fileLine = 'Case #' + str(t + 1) + ": " + str(Fraction(funValues[0])) + ' ' + str(funValues.count(funValues[0])) +'\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()
