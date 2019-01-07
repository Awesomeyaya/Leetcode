Given a 2d array A with 0s and 1s, 0 means sea and 1 means island. 
DFS can be used to find the island(area,perimeter,position).

1. Find island 
def DFS(i,j,A):
    if i < 0 or j < 0 or i == m or j == n or A[i][j] != 1:
        return None
    A[i][j] = -1
    DFS(i-1,j,A)
    DFS(i+1,j,A)
    DFS(i,j-1,A)
    DFS(i,j+1,A)
    
In this case, if DFS finds an island, it will be labeled with -1, and it will never be DFSed anymore.

2. Find position 
visited = [ [False] * col for i in range(row) ] 
q = Queue()
# create a 2D array with all items are False
def DFS(i,j,A,visited,q):
    if i < 0 or j < 0 or i == m or j == n or A[i][j] == 0 or visited[i][j] == True:
        return None
    visited[i][j] = True 
    q.put((x,y))
    DFS(i-1,j,A,visited,q)
    DFS(i+1,j,A,visited,q)
    DFS(i,j-1,A,visited,q)
    DFS(i,j+1,A,visited,q)
