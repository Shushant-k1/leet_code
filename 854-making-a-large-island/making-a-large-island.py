class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        d = {}
        component = 2
        count = {}
        n = len(grid)
        vis = set()
        for i in range(n) :
            for j in range(n) :
                if grid[i][j] == 1 and (i , j ) not in vis:
                    cnt = self.dfs(i , j , vis, grid , d , component)
                    count[component] = cnt
                    component += 1
        ans = 0
        for i in range(n) :
            for j in range(n) :
                if grid[i][j] == 0  :
                    temp = 0
                    se = set()
                    for x , y in [(-1 , 0) , (1 , 0) , (0 , 1) , (0 , -1)] :
                        if 0 <= x + i < len(grid) and 0 <= y + j < len(grid) and (x + i , y + j) in d:
                            se.add((d[(i+x , y+ j)]))
                    temp = 0
                    for k in se :
                        temp += count[k]
                    ans = max(ans , temp + 1)
                            
                    
        return ans if len(count) == 0 else max(ans , count[2])

    def dfs(self , i , j , vis , grid , d,component) :
        
        vis.add((i , j))
        d[(i , j)]  = component
        cnt = 1
        for x , y in [(-1 , 0) , (1 , 0) , (0 , 1) , (0 , -1)] :
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid) and grid[x+i][y+j] == 1 and (i + x , j+y) not in vis:
                
                cnt += self.dfs(i +x , j + y  , vis , grid , d,component)
        return cnt
