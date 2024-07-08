# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()
        n=len(nums)
        ans=float('inf')
        ans=min(ans,nums[n-4]-nums[0])
        ans=min(ans,nums[n-3]-nums[1])
        ans=min(ans,nums[n-2]-nums[2])
        ans=min(ans,nums[n-1]-nums[3])

        return ans