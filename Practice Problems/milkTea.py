inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

def recursiveFn(diff, tea, constraints, count, counts):
    j=0
    if "".join(tea) not in constraints:
        # print 'tea ====='
        # print tea
        # print count
        counts.append(count)
    while j<len(diff):
        l="".join(tea)
        if tea[diff[j][1]]  == '1':
            # x=(l + '.')[:-1]
            x=list(l)
            x[diff[j][1]] = '0'
        else:
            # x = (l + '.')[:-1]
            x=list(l)
            x[diff[j][1]] = '1'
        # print count
        count1 = count + diff[j][0]
        d = diff[0:j] + diff[j+1:]
        # print 'diff del'
        # print d
        # print x
        # print counts
        # print tea
        # print count
        # print '****************'
        counts = recursiveFn(d, x, constraints, count1, counts)
        j=j+1
    return counts


for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    # print line
    n = line[0]
    m=line[1]
    p = line[2]
    teas = []
    constraints = []
    i=0
    ones = [0]*p
    zeros = [0]*p
    tea = ''
    while i<n:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        j=0
        while j<p:
            if z[j] == '1':
                ones[j] = ones[j] +1
            else:
                zeros[j] = zeros[j]+1
            j=j+1
        teas.append(z)
        i=i+1
    i=0
    count = 0
    print 'case *********** ' + str(t)
    # print 'ones'
    # print ones
    # print 'zeros'
    # print zeros
    diff = [0]*p
    while i<p:
        if ones[i]>zeros[i]:
            tea=tea+'1'
            count = count +zeros[i]
            diff[i] = (ones[i]-zeros[i],i)
        else:
            tea = tea+'0'
            count = count + ones[i]
            diff[i] = (zeros[i] - ones[i],i)
        i=i+1
    diff = sorted(diff, key=lambda x: x[0])
    # print 'tea'
    # print tea
    # print 'count'
    # print count
    # print 'diff'
    # print diff
    i = 0
    while i < m:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        constraints.append(z)
        i = i + 1
    tea = list(tea)
    # print diff
    counts = recursiveFn(diff, tea, constraints, count, [])
    counts = sorted(counts)
    # print counts
    print counts[0]
    fileLine = 'Case #' + str(t + 1) + ": " + str(counts[0]) + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()