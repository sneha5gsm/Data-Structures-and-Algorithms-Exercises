# done
inputFile = open('inputFile', 'r')
outputFile = open('ceo_search_small_outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    people = int(inputFile.readline())
    n = 0
    count = []
    while n<people:
        n=n+1
        z = inputFile.readline()
        if z[len(z)-1] == '\n':
            z = z[: len(z) - 1]
        line = map(int, z.split(' '))
        # print line
        count.append((line[0], line[1]))
    # print 'count'
    # print count
    sortedArray = sorted(count, key=lambda x: x[1])
    # print sortedArray
    i=0
    j=1
    maxExperience = sortedArray[people -1][1]
    ceoExperience = 0
    k=0
    count1 =[]
    count2 = []
    while k < people:
        if sortedArray[k][1] !=0:
            count1.append(sortedArray[k][0])
            count2.append(sortedArray[k][0] * sortedArray[k][1])
        else:
            count1.append(sortedArray[k][0])
            count2.append(sortedArray[k][0])
        k = k +1
    flag = 0
    if people ==1:
        flag = 1
    total = 0
    # print 'cpount1'
    # print count1
    # print 'count2'
    # print count2
    while i<len(sortedArray):
        # print 'i'
        # print i
        # print 'j'
        # print j
        if flag ==0:
            if i<j:
                if count1[i]<count2[j]:
                    count1[i] = 0
                    count2[j] = count2[j] - count1[i]
                    i=i+1
                elif count1[i]>count2[j]:
                    count1[i] = count1[i] - count2[j]
                    count2[j] = 0
                    if j<(len(sortedArray)-1):
                        j=j+1
                    else:
                        total = total + count1[i]
                        flag = 1
                        i=i+1
                else:
                    count1[i] = 0
                    count2[j] = 0
                    if j<(len(sortedArray)-1):
                        j=j+1
                    else:
                        total = total + count1[i]
                        flag = 1
                    i=i+1
            else:
                if j < (len(sortedArray) - 1):
                    j = j + 1
                else:
                    total = total + count1[i]
                    flag = 1
                    i=i+1
        else:
            total = total + count1[i]
            # print 'total'
            # print total
            i=i+1
    #     print 'count1'
    #     print count1
    #     print 'count2'
    #     print count2
    # print 'total final'
    # print total
    # print 'maxexperience'
    # print maxExperience
    if (total)<(maxExperience+1):
        fileLine = 'Case #' + str(t + 1) + ": " + str(maxExperience + 1) + '\n'
        outputFile.write(fileLine)
    else:
        fileLine = 'Case #' + str(t + 1) + ": " + str(total) + '\n'
        outputFile.write(fileLine)
inputFile.close()
outputFile.close()

