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
                memo[state]=False
                return False
            if currsum == half or True in memo:
                memo[True]=True
                return True
            t = dp(i + 1, currsum + nums[i])
            l = dp(i + 1, currsum)
            memo[state] = t or l
            return memo[state]

        return dp(0, 0)
 