class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        if grid[n-1][n-1] == 1 or grid[0][0] == 1 :
            return -1

        dirs = [(-1 , 0 ), (1 , 0) , (0 , 1) , (0 , -1) , (-1 , -1) , (1 , 1) , (-1 , 1) , (1 , -1)]

        min_dist = 1

        q = deque()
        q.append((0 , 0))
        vis = set()
        vis.add((0 , 0))

        while q :
            for i in range(len(q)) :
                x , y = q.popleft()
                
                if x == n - 1 and y == n - 1 :
                    return min_dist
                for dr , dy in dirs :
                    nx , ny = x + dr , y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and (nx , ny) not in vis:
                        q.append((nx ,  ny))
                        vis.add((nx , ny))
            min_dist += 1
        
        return -1
        
