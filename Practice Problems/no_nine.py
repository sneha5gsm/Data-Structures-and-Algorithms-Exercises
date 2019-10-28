#done
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    start = line[0]
    end = line[1]
    count = 2
    j=start + (9-(start%9))
    if start == end:
        count = 1
    i=start + 1
    # print j
    while i< end:
        k=i
        flag =0
        # print 'i'
        # print i
        # print 'j'
        # print j
        if i != j:
            # k = str(i)
            # if k.count('9') == 0:
                # count=count+1
            # print "crossed first condition"
            temp=1
            x=1
            while i>0:
                if i%10 == 9:
                    temp = temp*x
                    flag = 1
                i= i/10
                x = x * 10
            if flag == 0:
                # print "crossed seconf condition"
                # print k
                count = count +1
                i=k+1
            else:
                if temp != 1:
                    f = temp - (k % temp)
                    i = f + k
                else:
                    i=k+1
        else:
            i=i+1
            j=j+9


        # print "i next"
        # print i

    fileLine = 'Case #' + str(t + 1) + ": " + str(count) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()