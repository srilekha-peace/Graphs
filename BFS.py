from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def add_Edge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,node):
        visited = [False]* self.vertices
        queue = []
        queue.append(node)
        visited[node] = True
        while queue:
            vert = queue.pop(0)
            print(vert, end = " ")
            for i in self.graph[vert]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph(4)
g.add_Edge(0,1)
g.add_Edge(0,2)
g.add_Edge(1,2)
g.add_Edge(2,0)
g.add_Edge(2,3)
g.add_Edge(3,3)
g.BFS(2)
