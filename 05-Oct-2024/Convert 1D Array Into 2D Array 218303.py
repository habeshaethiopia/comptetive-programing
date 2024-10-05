# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        s=0
        
        for i in range(m):
            ans.append(original[s:n+s])
            s+=n
        return ans if n*m==len(original) else [] 
        