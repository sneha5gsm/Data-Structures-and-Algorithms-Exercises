# time = 0
import sys
# print sys.getrecursionlimit()
sys.setrecursionlimit(1500)
def dfs(a, t):
    numberOfVertices = len(a)
    v = [0]*numberOfVertices
    i = 0
    p = [-1]*numberOfVertices
    # while i < numberOfVertices:
    #     i = i+1
    #     v.append(0)
    #     p.append(-1)
    i = 0
    while i< numberOfVertices:
        if v[i] == 0:
            dfsVisit(i, a, v,'',p, t)
        i=i+1

def bfs(a, cycle, vertex, fileLine):
    distance = 1000
    try:
        thing_index = cycle.index(vertex)
        distance = 0
    except ValueError:
        numberOfVertices = len(a)
        vertices = []
        i = 0
        queue = []
        roundFlag = 1000
        while i < numberOfVertices:
            vertices.append({'colour': 0, 'round': 0, 'vertex': i})
            i = i + 1
        queue.append(vertex)
        while len(queue) != 0:
            x = queue.pop(0)
            for k in a[x]:
                if vertices[k]['colour'] == 0 and vertices[k]['round'] <= roundFlag:
                    vertices[k]['colour'] = 1
                    try:
                        thing_index = cycle.index(k)
                        if distance > (vertices[x]['round'] + 1):
                            distance = vertices[x]['round'] + 1
                    except ValueError:
                        vertices[k]['round'] = vertices[x]['round'] + 1
                        queue.append(k)
    # print "distance:"+ str(vertex)
    # print distance
    fileLine = fileLine + ' ' + str(distance)
    return fileLine


def dfsVisit(b, a, v, path,p, t):
    # time = time + 1
    path = path + str(b) + ','
    v[b] = 1
    for x in a[b]:
        if v[x] == 0:
            p[x] = b
            dfsVisit(x, a, v, path,p,t)
        elif v[x] == 1 and p[b] != x:
            path = path + str(x) + ','
            path = path[: len(path) - 1]
            cycle = [int(e) for e in path.split(',')]
            cycle = cycle[cycle.index(cycle[len(cycle)-1]):-1]
            j=0
            fileLine = 'Case #' + str(t + 1) + ":"
            while j< len(a):
                fileLine = bfs(a,cycle,j, fileLine)
                j=j+1
            fileLine = fileLine + '\n'
            outputFile.write(fileLine)
            break
    v[b] = 2

dfs([[1],[0,2,3],[1,3,4],[1,2],[2]],0)
# inputFile = open('inputFile', 'r')
# outputFile = open('outputFile', 'w+')
# testCases = int(inputFile.readline())
#
# for t in range(0, testCases):
#     numberOfPlanets = int(inputFile.readline())
#     a = []
#     b=0
#     while b< numberOfPlanets:
#         a.append([])
#         b=b+1
#     j = 0
#     while j<numberOfPlanets:
#         j=j+1
#         z = inputFile.readline()
#         if z[len(z) - 1] == '\n':
#             z = z[: len(z) - 1]
#         connection = map(int, z.split(' '))
#         a[connection[0] - 1].append(connection[1] - 1)
#         a[connection[1] - 1].append(connection[0] - 1)
#     # print 'case ' + str(t+1)+'a'
#     # print a
#     dfs(a,t)


