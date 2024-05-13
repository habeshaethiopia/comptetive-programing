# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i,cursum):
            # print(i, cursum)
            if cursum == target and i==len(nums):
                return 1
            ret=0
            if i<len(nums):
                p=dp(i+1,cursum+nums[i])
                n=dp(i+1,cursum-nums[i])
                ret+=n+p
            return ret
        return dp(0,0)

                


            

