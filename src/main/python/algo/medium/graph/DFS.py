from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def traverseDFS(self, v):
        self.visited.add(v)
        print(v)
        for e in self.graph[v]:
            if e not in self.visited:
                self.traverseDFS(e)

    def traverse(self):
        for k in self.graph:
            if k not in self.visited:
                self.traverseDFS(k)
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.traverse()