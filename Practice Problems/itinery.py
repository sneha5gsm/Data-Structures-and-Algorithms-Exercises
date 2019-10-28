class Node(object):
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    n = int(inputFile.readline())
    i=0
    airportString = ''
    airportString2 = ''
    nodes = []
    while i<n:
        z = inputFile.readline()
        if z[len(z)-1] == '\n':
            z = z[: len(z) - 1]
        airportStart = z
        z = inputFile.readline()
        if z[len(z)-1] == '\n':
            z = z[: len(z) - 1]
        airportEnd = z
        nodes.append((airportStart,airportEnd))
        airportString2 = airportString2 + airportStart + '-' + str(i) + ' '
        i = i+1
        airportString = airportString + airportEnd + ' '
    # print 'airportstring'
    # print airportString
    i=0
    fileLine = 'Case #' + str(t + 1) + ": "
    while i<n:
        if nodes[i][0] not in airportString:
            node = nodes[i]
            searchString = node[0] + '-'
            searchIndex = airportString2.find(searchString) + len(searchString)
            while searchIndex != -1:
                node = nodes[int(airportString2[searchIndex])]
                fileLine = fileLine + str(node[0]) + '-' + str(node[1]) + ' '
                searchString = node[1] + '-'
                if searchString in airportString2:
                    searchIndex = airportString2.find(searchString) + len(searchString)
                else:
                    searchIndex = -1
            break
        i=i+1
    fileLine = fileLine + '\n'
    outputFile.write(fileLine)
inputFile.close()
outputFile.close()

