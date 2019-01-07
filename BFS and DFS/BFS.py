Usually, a problem can be solved with both DFS and BFS.
BFS focus on queue. 

For example, for the island problem. BFS can find the area, perimeter and position of the island.

1.Find the perimeter of an island
def sum(i,j):
    res = 0
    adjacent = (i-1,j),(i+1,j),(i,j-1),(i,j+1),
    for x,y in adjacent:
        if x < 0 or y < 0 or x == m or y == n or A[x][y] == 0:
            res +=1
    return res 
    
2.Find the area of an island 

        
    
