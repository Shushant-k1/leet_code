class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = -1
        for i in range(len(matrix)) :
            if matrix[i][0] <= target and matrix[i][-1] >= target :
                row = i
                break
        
        if row == -1 : return False

        mat_to_search = matrix[i]
        print(mat_to_search)
        l = 0
        h = len(mat_to_search) 

        while l < h :
            mid = (l + h) // 2
            if mat_to_search[mid] == target :
                return True
            elif mat_to_search[mid] > target :
                h = mid 
            else :
                l = mid  + 1
        
        return False