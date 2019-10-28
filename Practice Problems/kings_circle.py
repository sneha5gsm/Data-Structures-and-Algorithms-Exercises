from collections import Counter
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n= line[0]
    v1=line[1]
    h1 = line[2]
    a =line[3]
    b=line[4]
    c=line[5]
    d =line[6]
    e=line[7]
    f = line[8]
    m=line[9]
    i=1
    pointArray = []
    pointArray.append((v1,h1))
    while i<n:
        x=(a*v1 + b*h1 + c)%m
        y=(d*v1 + e*h1 + f)%m
        v1=x
        h1=y
        pointArray.append((v1,h1))
        i=i+1
    xarray = sorted(pointArray, key=lambda x: x[0])
    yarray = sorted(pointArray, key=lambda x: x[1])

    # print 'point array sorted'
    # print pointArray
    i=0
    counterx = Counter(elem[0] for elem in pointArray)
    countery = Counter(elem[1] for elem in pointArray)
    index = 0
    if len(counterx) >len(countery):
        counter =  countery
        pointArray = yarray
        index=1
    else:
        pointArray = xarray
        counter = counterx
    # print 'countetr'
    # print counter
    i=0
    j=0
    k=0
    count =0
    # print 'n'
    # print n
    # print 'pointarray'
    # print pointArray
    while i<n:
        j=i +1
        # print 'i'
        # print i
        # print 'counter[pointArray[i][index]'
        # print counter[pointArray[i][index]]
        if counter[pointArray[i][index]] >1:
            y= n -(i+2)
            while y>1:
                count = count + (y)*(y+1)/2
                y=y-1
            if y ==1:
                count = count + 1
            i=i+counter[pointArray[i][index]]
            # print 'i'
            # print i
        else:
            while j<n:
                k=j+1
                if pointArray[i][0]==pointArray[j][0] or pointArray[i][1]==pointArray[j][1]:
                    count = count + (n-k)
                else:
                    while k<n:
                        # print 'i'
                        # print i
                        # print 'j'
                        # print j
                        # print 'k'
                        # print k
                        if pointArray[i][0]==pointArray[j][0] or pointArray[i][0] == pointArray[k][0] or pointArray[j][0]==pointArray[k][0]:
                            count = count+1
                        else:
                            if pointArray[i][1]==pointArray[j][1] or pointArray[i][1] == pointArray[k][1] or pointArray[j][1]==pointArray[k][1]:
                                count =count +1

                        k=k+1
                j=j+1
            i=i+1
    print 'count'
    print count
    fileLine = 'Case #' + str(t + 1) + ": " + str(count) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()