class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis = set()
        adj = image[sr][sc]
        image[sr][sc] = color
        self.dfs(image , vis , sr ,sc , color , adj)
        return image

        
    
    
    def dfs(self , image ,vis , sr , sc , color , adj ) :

        dirs = [(-1 , 0) , (1 , 0) , (0 , 1) , (0 ,-1)]
        for x , y in dirs :
            new_x , new_y = sr  + x, sc + y
            if (new_x , new_y )not in vis and 0 <= new_x <len(image) and 0 <= new_y < len(image[0]) and image[new_x][new_y] == adj:

                image[new_x][new_y] = color
                vis.add((new_x , new_y))
                self.dfs(image , vis , new_x , new_y , color , adj)