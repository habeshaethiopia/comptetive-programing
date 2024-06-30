# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans=1
        i=0
        while i< len(nums):
            t=nums[i]-1
            if t<len(nums) and t>=0:
                if ans ==t+1:
                    ans +=1
                if t==i:
                    i+=1
                else:
                    if nums[i] == nums[t]:
                        i+=1
                    else:
                        nums[i], nums[t]= nums[t], nums[i]
            else:
                i+=1
        ans=1
        i=0
        while i< len(nums):
            t=nums[i]-1
            if t<len(nums) and t>=0:
                if ans ==t+1:
                    ans +=1
                if t==i:
                    i+=1
                else:
                    if nums[i] == nums[t]:
                        i+=1
                    else:
                        nums[i], nums[t]= nums[t], nums[i]
            else:
                i+=1
        return ans