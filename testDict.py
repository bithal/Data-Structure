'''
#dynamic dict
d={}
k = input("key : ")
v= input('value : ')
d[k]=v
print(d)
'''


#'''
#list of objects
class Nodes:
    def __init__(self,node):
        self.node = node
        self.points = None

def fun(dict,key,value):
    dict[key] = value
x = {}
y=Nodes(4)
z = Nodes(5)
a = Nodes(3)

fun(x,y,z)
fun(x,a,y)
for i in x:
    print(x[i].node,x[i].node)
#'''
