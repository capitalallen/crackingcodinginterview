import time
"""
getpath: return path
input: maze
"""
def findpath(maze):
    path = []
    if maze == None or len(maze) == 0:
        return None
    if getPath(maze,len(maze)-1,len(maze[0])-1,path):
        return path
    return None

"""
if col or row or maze[r][c] = true
return false
isatorigin:
- boolean row==0 or col==0
if isatorigin or getpath r,c-1 or getpant r-1,c,path
path.append((r,c))
"""
def getPath(maze,row,col,path):
    if col <0 or row<0 or maze[row][col]:
        return False
    isAtOrigin = (row==0) and (col==0)

    if isAtOrigin or getPath(maze,row,col-1,path) or getPath(maze,row-1,col,path):
        p = (row,col)
        path.append(p)
        return True
    return False
def dpfindpath(maze):
    if maze == None or len(maze) == 0:
        return None
    failedpath = set()
    path = []
    if dpgetpath(maze,len(maze)-1,len(maze[0])-1,path,failedpath):
        return path
    return None

def dpgetpath(maze,row,col,path,failedpath):
    if col <0 or row < 0 or maze[row][col]:
        return False
    p = (row,col)

    if p in failedpath:
        return False
    
    isAtOrigion = (row==0) and (col==0)

    if (isAtOrigion or dpgetpath(maze,row,col-1,path,failedpath) or dpgetpath(maze,row-1,col,path,failedpath)):
        path.append(p)
        return True
    failedpath.add(p)
    return False

maze = [
            [False,False,False,False],
            [False,False,True,False],
            [False,True,True,False],
            [False,False,True,False]
]
start = time.time()
a = findpath(maze)
end = time.time()
print(a)
print(end-start)
start = time.time()
b = dpfindpath(maze)
end = time.time()
print(end-start)
print(b)