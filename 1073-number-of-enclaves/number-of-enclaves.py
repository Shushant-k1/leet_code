class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        

        nodes = []

        m , n = len(grid) , len(grid[0])
        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == 1 and (i == 0 or j  == 0 or i == m - 1 or j == n - 1) :
                    nodes.append((i, j))


                    
        vis = set()
        print(nodes)
        for node in nodes :
            if node not in vis :
                self.dfs(grid , node  , vis)
        cnt = 0
        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == 1  and (i , j) not in vis :
                    cnt += 1
        return cnt

        
    def dfs(self , grid , cur , vis) :
        vis.add(cur)
        dirs = [(0 , 1) , (1 , 0) , (-1 , 0) , (0 , -1)]
        dx , dy = cur
        for x , y in dirs :
            nx , ny = x + dx , y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx , ny) not in vis :
                self.dfs(grid , (nx , ny) , vis)
