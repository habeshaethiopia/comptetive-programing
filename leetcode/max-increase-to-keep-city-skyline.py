class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # mtx=[[0]*len(grid[0] for _ in grid]
        ans=0
        row=[]
        col=[]
        for i in range(len(grid)):
            row.append(max(grid[i]))
            cm=0
            for j in range(len(grid[0])):
                cm=max(cm,grid[j][i])
            col.append(cm)
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans+=min(row[i],col[j])-grid[i][j]
        return ans

