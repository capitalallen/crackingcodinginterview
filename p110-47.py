from collections import defaultdict

#adjacency list 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def printGraph(self):
        print(self.graph)
    def topology_sort(self,v,arr,visited_list):
        """
        if vertix is not visited: mark vertix as True, for each neighbor of vertix, recursion, append vertix to arr
        """
        if not visited_list[v]:
            visited_list[v] = True
            for neighbor in self.graph[v]:
                if neighbor != None:
                    self.topology_sort(neighbor,arr,visited_list)
            return arr.append(v) 
    def buildOrder(self):
        """
        output: arr
        visited_list: typle: defaultdict, vertix: True/False
        for loop: call topology for each vertix
        """
        arr = []
        visited_list = defaultdict()
        for i in self.graph:
            visited_list[i] = False    
        for i in visited_list:
            self.topology_sort(i,arr,visited_list)
        print(arr[::-1])
g = Graph()
g.addEdge('a', 'd')
g.addEdge('f', 'b')
g.addEdge('b', 'd')
g.addEdge('f', 'a')
g.addEdge('d', 'c')
g.addEdge('e',None)
g.addEdge('c',None)
g.printGraph()
g.buildOrder()

