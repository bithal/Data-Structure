from collections import defaultdict

class Node:
    def __init__(self,name,wt = None):
        self.name = name
        self.wt = wt

class Graph:
    def __init__(self):
         self.graph = defaultdict(list)

    def addEdge(self,edge):
        c = 0
        if self.graph:
            for i in self.graph:
                if i.name == edge[0]:
                    dstn = Node(edge[1],edge[2])
                    self.graph[i].append(dstn)
                    c = 1
        else:
            src = Node(edge[0])
            dstn = Node(edge[1],edge[2])
            self.graph[src] = []
            self.graph[src].append(dstn)
            c = 1

        if c == 0:
            src = Node(edge[0])
            dstn = Node(edge[1],edge[2])
            self.graph[src] = []
            self.graph[src].append(dstn)

    def print_graph(self):
        for i in self.graph:
            print(i.name,end=' ')
            for j in range(0,len(self.graph[i])):
                print(self.graph[i][j].name,self.graph[i][j].wt,end=' ')
            print()

if __name__=='__main__':
    g = Graph()
    line = []
    with open('Graph_AdjMatrix.txt','r') as fp:
        for line in fp:
            edge = line.split()

            g.addEdge(edge)
    g.print_graph()
