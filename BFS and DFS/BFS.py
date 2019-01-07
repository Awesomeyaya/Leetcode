Usually, a problem can be solved with both DFS and BFS.
BFS focus on queue. 

For example, for the island problem. BFS can find the area, perimeter of the island, also the shortese bridge between two islands.

1.Find the perimeter of an island
def sum(i,j):
    res = 0
    adjacent = (i-1,j),(i+1,j),(i,j-1),(i,j+1),
    for x,y in adjacent:
        if x < 0 or y < 0 or x == m or y == n or A[x][y] == 0:
            res +=1
    return res 
    
2.Find the shortest bridge 
... Firstly we use DFS to find the positions of an island using visited matrix. 
Then we get a queue q with the positions of the island. 
dist = 0
while not q.empty():
    size = q.qsize()
    for i in range(size):
        r,l = q.get()
        adjacent = (r-1,l),(r+1,l),(r,l-1),(r,l+1),
        for x,y in adjacent:
            if 0<=x<m and 0<=y<n and visited[x][y] == False:
                if A[x][y] == 1:
                    return dist
                else:
                    q.put((x,y))
                    visited[x][y] = True
        dist += 1
return -1


        
    
