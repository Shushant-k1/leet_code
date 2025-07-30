class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])

        rotten =  []
        cnt = 0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 2 :
                    rotten.append((i ,j))
                elif grid[i][j] ==1 :
                    cnt += 1
        
        vis = set()
        dirs = [(0 , -1) , (0 , 1) , (1 , 0) , (-1 , 0)]
        time = 0
        while rotten and cnt :
            time += 1
            for i in range(len(rotten)) :
                dx , dy = rotten.pop(0)
                for x , y in dirs :
                    new_x , new_y = x + dx , y + dy
                    if 0 <= new_x < n and 0<= new_y < m and grid[new_x][new_y] == 1 and (new_x , new_y) not in vis :
                        vis.add((new_x , new_y))
                        rotten.append((new_x, new_y))
                        cnt -= 1
        return -1 if cnt > 0 else time

        
