class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        col=len(matrix[0])
        R=len(matrix)*len(matrix[0])-1
        while L<=R:
            mid=(L+R)//2
            c=mid%col
            r=mid//col

            if  matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                L=mid+1
            else:
                R=mid-1
        return False