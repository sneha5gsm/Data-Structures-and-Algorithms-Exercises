inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    numberString = inputFile.readline()
    if numberString[len(numberString) - 1] == '\n':
        numberString = numberString[: len(numberString) - 1]
    numberArray = map(int, numberString)
    number = int(numberString)
    # print number
    if len(numberArray) == 1:
        fileLine = 'Case #' + str(t + 1) + ": " + '1' + '\n'
        outputFile.write(fileLine)
    else:
        j=0
        flag = 0
        flag2=0
        while j < len(numberArray):
            if numberArray[j]%2!=0:
                flag = 1
                # print 'j'
                # print j
                # print numberArray[j]
                tenPow = pow(10,len(numberArray) - (j))
                # print 'tenPow'
                # print tenPow
                otherTenPow = pow(10, len(numberArray)-j-1)
                z = number%tenPow
                # print 'z'
                # print z
                w = number/tenPow
                # print 'w'
                # print w

                if j!=0 and numberArray[j] == 9:
                    print 'inside if of 9'
                    x1 = (numberArray[j-1] +1) * otherTenPow *10
                    x = x1 - number%(tenPow *10)
                    flag2=1
                    print 'x1'
                    print x1
                    print 'x'
                    print x
                else:
                    x1 = (numberArray[j]+1) * otherTenPow
                    x =  x1 - z
                if len(numberArray)-j-1 !=0:
                    y1 = (numberArray[j]-1) * otherTenPow + int('8'*(len(numberArray)-j-1))
                else:
                    y1 = (numberArray[j]-1) * otherTenPow
                y = z -y1
                if x>y:
                    # print 'inside if'
                    # print str(number - (w*tenPow + y1))
                    fileLine = 'Case #' + str(t + 1) + ": " + str(number - (w*tenPow + y1)) + '\n'
                    outputFile.write(fileLine)
                else:
                    if flag2==0:
                        fileLine = 'Case #' + str(t + 1) + ": " + str((w * tenPow + x1) - number) + '\n'
                        outputFile.write(fileLine)
                    else:
                        print 'number to subtract from'
                        print str(((number/(tenPow*10)) * tenPow *10 + x1))
                        fileLine = 'Case #' + str(t + 1) + ": " + str(((number/(tenPow*10)) * tenPow *10 + x1) - number) + '\n'
                        outputFile.write(fileLine)
                break
            j=j+1
        if flag == 0:
            fileLine = 'Case #' + str(t + 1) + ": " + '0' + '\n'
            outputFile.write(fileLine)

inputFile.close()
outputFile.close()





