inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

def recursiveFn(cards, sum):
    print 'cards'
    print cards
    # print 'sum'
    # print sum
    if len(cards) >1:
        i=1
        minimum = 2147483647
        while i<len(cards):
            # print 'len cards'
            # print len(cards)
            # print '==========================='
            # print cards
            # print i
            # print 'cards[0][1]^cards[i][0]'
            # print cards[0][1]^cards[i][0]
            # print cards[0][0]^cards[i][1]
            # print '================================='
            val = sum + min(cards[0][0]^cards[i][1], cards[0][1]^cards[i][0])
            print 'val before rec'
            print val
            val = min(recursiveFn(cards[1:],val), recursiveFn(cards[:i] + cards[(i+1):], val))
            print 'val after'
            print val
            if val < minimum:
                minimum = val
            i=i+1
        print 'minimum'
        print minimum
    else:
        minimum = sum
    return minimum



for t in range(0, testCases):
    n = int(inputFile.readline())
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    reds = map(int, z.split(' '))
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    blues = map(int, z.split(' '))
    i=0
    cards = []
    while i<n:
        cards.append((reds[i], blues[i]))
        i=i+1
    outputFile.write('Case #' + str(t + 1) + ": " + str(recursiveFn(cards, 0)) + '\n')
inputFile.close()
outputFile.close()


