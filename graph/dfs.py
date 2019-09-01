from collections import defaultdict

#adjacency list 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def printGraph(self):
        return self.graph
    def DFSUtil(self,v,visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i,visited)
    def DFS(self,v):
        visited = [False]*len(self.graph)
        self.DFSUtil(v,visited)
    def DFSAllNodes(self,v):
        visited = [False]* len(self.graph)
        for i in range(len(self.graph)):
            if visited[i] == False:
                self.DFSUtil(i,visited)
    def BFS(self,s):
        #visited list = False
        # queue = []
        # append s to queue
        # mark visited[s] = true
        # when queue is not empty
        # s = top of queue
        #print s
        #for i in graph[s]

        visited = [False]*len(self.graph)
        result = []
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            result.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return result
    def findRoute(self,u,v):
        l = self.BFS(u)
        if u in l and v in l:
            return True
        else:
            return False
# Create a graph given 
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
# g.DFS(2)
# g.BFS(2)
a= g.findRoute(1,3)
b= g.findRoute(1,4)
print(a,b)