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

def DFS(self,start,visited):
    visited.append(start.name)
    print(start.name)

    for i in self.graph[self.retn_obj(start)]:
        if i.name not in visited:
            self.dfs(i,visited)

if __name__=="__main__":
    graph.Graph.dfs = DFS
    graph.Graph.retn_obj = return_object
    create_graph(g)
    visited = []
    for i in g.graph:
        if i.name == 'A':
            break
    g.dfs(i,visited)

    for i in g.graph:
        if i.name not in visited:
            g.dfs(i,visited)
