# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         cnt = 0
#         for i in range(len(grid)) :
#             c = 0
#             for j in range(len(grid[0])) :
#                 if grid[i][j] == 1 :
#                     c += 1
#                     grid[i][j] = -1
#             if c > 1 :
#                 cnt += c
        
#         for i in range(len(grid[0])) :
#             c = 0
#             for j in range(len(grid)) :
#                 if grid[i][j] == -1  or grid[i][j] == 1:
#                     c += 1
                
#             if c > 1 :
#                 for j in range(len(grid)) :
#                     if grid[i][j] == 1 :
#                         c += 1
#             cnt += c
#         return c

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt = 0
        
        for i in range(len(grid)):
            row_count = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_count += 1
            if row_count > 1:
                for j in range(len(grid[0])) :
                    if grid[i][j] == 1 :
                        grid[i][j] = -1  # Mark the servers in the row as counted
                cnt += row_count
        
        # Second pass: Count servers in each column
        for j in range(len(grid[0])):
            col_count = 0
            for i in range(len(grid)):
                if grid[i][j] == -1 or grid[i][j] == 1:  # Consider servers that are not counted yet
                    col_count += 1
            
            if col_count > 1:
                for i in range(len(grid)):
                    if grid[i][j] == 1:  # Only count servers that are still unmarked
                        cnt += 1
        
        return cnt
