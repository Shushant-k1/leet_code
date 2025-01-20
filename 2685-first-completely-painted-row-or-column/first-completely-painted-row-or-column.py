class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        d = {}
        for i in range(len(mat)) :
            for j in range(len(mat[0])) :
                d[mat[i][j]] = (i , j)
        
        x_row = {} 
        x_col = { }

        for i in range(len(arr)) :
            row , col = d[arr[i]]
            if row not in x_row :
                x_row[row] = []
            
            if col not in x_col :
                x_col[col] = []
            x_row[row].append(arr[i])
            x_col[col].append(arr[i])

            if len(x_row[row]) == len(mat[0]) :
                return i
            if len(x_col[col]) == len(mat) :
                return i
        return len(arr) - 1


