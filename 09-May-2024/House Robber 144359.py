# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def __init__(self):
        self.mem = {}

    def rob(self, nums: List[int]) -> int:
       
        
        dp={0:nums[0]}
        def back(i):
            if i ==1:
                dp[i]=max(nums[0],nums[1])
            elif i not in dp:
                dp[i]=max(back(i-1),nums[i]+back(i-2))
            return dp[i]
         
        return back(len(nums)-1)
       
