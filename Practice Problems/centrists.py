# done
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    nameSize = int(inputFile.readline())
    i = 0
    possibility = ['x', 'x', 'x']
    alphabetOrder = []
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    names = map(str, z.split(' '))
    print 'names'
    print names
    deviated = 'a'
    while i<nameSize:
        print 'i'
        print i
        print names[0][i]
        print names[1][i]
        print names[2][i]
        if names[0][i] == names[1][i] == names[2][i] and possibility.count('x') == 3:
            print 'inside one'
            i = i + 1
        elif names[0][i] == names[1][i] and possibility[0]=='x' and possibility[1]=='x':
            print 'inside 2'
            possibility[2] = 'NO'
            deviated = names[2][i]
            alphabetOrder.append(names[0][i])
            alphabetOrder.append(names[2][i])
            i=i+1
        elif names[0][i] == names[2][i] and possibility[0]=='x' and possibility[2]=='x':
            print 'inside 3'
            possibility[1] = 'NO'
            deviated = names[1][i]
            alphabetOrder.append(names[0][i])
            alphabetOrder.append(names[1][i])
            i=i+1
        elif names[1][i] == names[2][i] and possibility[1]=='x' and possibility[2]=='x':
            print 'inisde four'
            possibility[0] = 'NO'
            deviated = names[0][i]
            alphabetOrder.append(names[2][i])
            alphabetOrder.append(names[0][i])
            i=i+1
        elif possibility.count('x') == 0:
            break
        elif names[1][i] != names[2][i] and names[1][i] != names[0][i] and names[0][i] != names[2][i] and possibility.count('x') == 3:
            possibility[0] = 'YES'
            possibility[1] = 'YES'
            possibility[2] = 'YES'
            break
        else:
            print 'inside else'
            j=0
            m=[]
            while j<3:
                if possibility[j] == 'x':
                        m.append(j)
                j=j+1
            if names[m[0]][i] == names[m[1]][i]:
                i=i+1
            else:
                if alphabetOrder.count(names[m[0]][i])==0 or alphabetOrder.count(names[m[1]][i]) == 0:
                    possibility[m[0]] = 'YES'
                    possibility[m[1]] = 'YES'
                elif names[m[0]].count(deviated) < names[m[1]].count(deviated):
                    possibility[m[0]] = 'NO'
                    possibility[m[1]] = 'YES'
                else:
                    possibility[m[0]] = 'YES'
                    possibility[m[1]] = 'N0'
        print 'possibility'
        print possibility
    fileLine = 'Case #' + str(t + 1) + ": " + possibility[0] + ' ' + possibility[1] + ' ' + possibility[2] + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()



