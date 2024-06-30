# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        c=0
        while(l<r):
            if nums[l]+nums[r]==k:
                c+=1
                l+=1
                r-=1
            if nums[l]+nums[r]>k:
                r-=1
            if nums[l]+nums[r]<k:
                l+=1
        return c