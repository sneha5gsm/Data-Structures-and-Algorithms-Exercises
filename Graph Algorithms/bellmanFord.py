class creategraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellmanFord(self, src):
        distances = [float("Inf")] * self.vertices
        distances[src] = 0
        for v in range(self.vertices - 1):
            for u, v, w in self.graph:
                x = distances[u] + w
                if distances[u] != float('inf') and x < distances[v]:
                    distances[v] = x
        for u, v, w in self.graph:
            x = distances[u] + w
            if distances[u] != float('inf') and x < distances[v]:
                print('graph contains a negative weight cycle')
                return
        print(distances)


g = creategraph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
g.bellmanFord(0)