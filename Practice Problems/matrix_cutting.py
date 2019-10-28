inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

def recursiveFn(matrix, n1, n2, m1, m2,sum, dictionary):
    # print '+++++++++++++'
    # print dictionary
    minimum = 2147483647
    x=str(n1)+str(n2)+str(m1)+str(m2)
    # print x
    if x in dictionary:
        return dictionary[x]
    elif n2-n1 ==0 and m2-m1==0:
        # print 'inside elif 0'
        return 0
    elif n2-n1==0:
        # print 'inside elif n'
        i = m1
        while i <= m2:
            if matrix[n1][i] < minimum:
                minimum = matrix[n1][i]
            i = i + 1
        sum = minimum
        # print 'minimum'
        # print minimum
        i = m1
        minimum2 = -1
        while i < m2:
            value = sum + recursiveFn(matrix, n1, n2, m1, i, sum, dictionary) + recursiveFn(matrix, n1, n2, i + 1, m2, sum, dictionary)
            if value > minimum2:
                minimum2 = value
            i=i+1
        dictionary[x]=minimum2
        # print 'minimum2'
        # print minimum2
        return minimum2
    elif m2-m1==0:
        # print 'inside elif m'
        i = n1
        while i <= n2:
            if matrix[i][m1] < minimum:
                minimum = matrix[i][m1]
            i = i + 1
        sum = minimum
        # print 'minimum'
        # print minimum
        # print 'sum'
        # print sum
        i = n1
        minimum2 = -1
        while i < n2:
            value = sum + recursiveFn(matrix, n1,i,m1, m2, sum, dictionary ) + recursiveFn(matrix, i+1,n2, m1,m2,sum, dictionary)
            if value > minimum2:
                # print 'va;ue'
                # print value
                minimum2 = value
            i=i+1
        dictionary[x] = minimum2
        # print 'minimum2'
        # print minimum2
        return minimum2
    else:
        # print 'inside else'
        i=n1
        while i<=n2:
            j=m1
            while j<=m2:
                if matrix[i][j] < minimum:
                    minimum = matrix[i][j]
                j=j+1
            i=i+1
        sum = minimum
        # print 'sum'
        # print sum
        i=n1
        minimum2 = -1
        while i<n2:
            value  = sum + recursiveFn(matrix, n1,i,m1, m2, sum, dictionary ) + recursiveFn(matrix, i+1,n2, m1,m2,sum, dictionary)
            if value > minimum2:
                # print 'value'
                # print value
                minimum2 = value
            i=i+1
        i=m1
        while i< m2:
            value = sum + recursiveFn(matrix, n1,n2,m1, i, sum,dictionary ) + recursiveFn(matrix, n1,n2, i+1,m2,sum, dictionary)
            if value > minimum2:
                minimum2 = value
            i=i+1
        dictionary[x] = minimum2
        return minimum2


for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n = line[0]
    m = line[1]
    matrix = []
    i=0
    while i<n:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        matrix.append(map(int, z.split(' ')))
        i=i+1
    # print 'matrix'
    # print matrix
    # print n
    # print m
    outputFile.write('Case #' + str(t + 1) + ": " + str(recursiveFn(matrix, 0,n-1, 0, m-1, 0, {})) + '\n')
inputFile.close()
outputFile.close()