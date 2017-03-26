import Graph_AdjMatrix as graph

g = graph.Graph()

def create_graph(g):
    line = []
    with open('Graph_AdjMatrix.txt','r') as fp:
        for line in fp:
            edge = line.split()
            g.addEdge(edge)

def return_object(self,obj):
    for i in self.graph:
        if i.name == obj.name:
            return i


def BFS(self,start,visited):

    queue = []

    visited.append(start.name)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex.name)
        vertex = self.retn_obj(vertex)

        for i in self.graph[vertex]:
            if i.name not in visited:
                visited.append(i.name)
                queue.append(i)

if __name__ == '__main__':
    visited = []
    graph.Graph.bfs = BFS
    graph.Graph.retn_obj = return_object
    create_graph(g)

    for i in g.graph:
        if i.name == 'A':
            break
    g.bfs(i,visited)

    for i in g.graph:
        if i.name not in visited:
            g.bfs(i,visited)
