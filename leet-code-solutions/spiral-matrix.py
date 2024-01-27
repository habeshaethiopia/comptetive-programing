class Solution(object):
    def spiralOrder(self,matrix):
        if not matrix:
            return []
        
        result = []
        row_start = 0
        row_end = len(matrix) - 1
        col_start = 0
        col_end = len(matrix[0]) - 1
        
        while row_start <= row_end and col_start <= col_end:
            # Traverse top row
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1
            
            # Traverse right column
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            
            # Traverse bottom row
            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            
            # Traverse left column
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
        
        return result
            