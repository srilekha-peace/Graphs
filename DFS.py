from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def add_Edge(self,u,v):
        self.graph[u].append(v)

    def DFS(self):
        visited = [False]* self.vertices

        for i in range(self.vertices):
            if visited[i] == False:
                self.helper_func(i, visited)

    def helper_func(self,node, visited):
        visited[node] = True
        print(node, end = " ")

        for i in self.graph[node]:
            if visited[i] == False:
                self.helper_func(i, visited)

g = Graph(4)
g.add_Edge(0,1)
g.add_Edge(0,2)
g.add_Edge(1,2)
g.add_Edge(2,0)
g.add_Edge(2,3)
g.add_Edge(3,3)
g.DFS()
