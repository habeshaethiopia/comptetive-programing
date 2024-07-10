# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        mx=0
        for i in range(len(points)-1):
            mx=max(mx,points[i+1][0]-points[i][0])
        return mx