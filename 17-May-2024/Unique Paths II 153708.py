# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''bottom up'''
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        def check(i,j):
            return i>=0 and j>=0 and i<m and j<n and not obstacleGrid[i][j]
        pre=[[0]*n for i in range(m)]
        if not obstacleGrid[0][0]:
            pre[0][0]=1
        else: 
            return 0
        # print(pre)
        for i in range(m):
            for j in range(n):
                # print(pre)
                if check(i,j):
                    pre[i][j]+=pre[i][j-1] if check(i,j-1) else 0 
                    pre[i][j]+=pre[i-1][j] if check(i-1,j) else 0 

            # print('***',pre)
            
        return pre[-1][-1]