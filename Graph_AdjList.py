class Nodes:
    def __init__(self,node):
        self.node = node
        self.next = None

class Graph:
    def __init__(self):
        self.head = None

    def Adj_List(self,data):
#        print('in Adj_List()')
        for i in data:
            node = Nodes(i)
#            print(node.node,node.next)
            if self.head is None:
                self.head = node
#                print(self.head.node,self.head)
            else:
                last = self.head
#                print(last.node,last.next)
                while last.next:
#                    print(last.node,last.next)
                    last= last.next
                last.next = node


    def print_graph(self):
        #print('sdfs')
        last = self.head
        while last:
            print(last.node,end=' ')
#            print('sdfdsf')
            last =last.next
        print()

if __name__=='__main__':
    file = open('Graph.txt','r')
    adjList = []
    for l in file:
        nodes = l.split()
        x = Graph()
        x.Adj_List(nodes)
        adjList.append(x)

    print(type(adjList))
    for i in adjList:
        i.print_graph()
    #graph.print_Adj_List(allNodes)
