import sys

class createGraph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph  = [[0 for column in range(vertices)] for row in range(vertices)]

    def minDistance(self, distances, sptSet):
        min = sys.maxsize
        minindex = -1
        for i in range(self.vertices):
            if distances[i] < min and sptSet[i] == False:
                min = distances[i]
                minindex = i
        return minindex


    def djikstras(self, src):
        sptSet = [False] * self.vertices
        distances = [sys.maxsize] * self.vertices
        distances[src] = 0
        for v in range(self.vertices):
            u = self.minDistance(distances, sptSet)
            sptSet[u] = True

            for x in range(self.vertices):
                if self.graph[u][x] > 0 and sptSet[x] == False and distances[u] + self.graph[u][x] < distances[x]:
                    distances[x] = distances[u] + self.graph[u][x]
        print(distances)


g = createGraph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.djikstras(0);


