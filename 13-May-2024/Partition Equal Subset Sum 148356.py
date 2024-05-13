# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2:
            return False
        half = sm // 2

        memo = {}

        def dp(i, currsum):
            state = (i, currsum)
            if state in memo :
                return memo[state]
            
            if i == len(nums) or currsum > half:
                return False
            if currsum == half :
                # memo[True]=True
                return True
           
            memo[state] = dp(i + 1, currsum + nums[i]) or dp(i + 1, currsum)
            return memo[state]

        return dp(0, 0)
 