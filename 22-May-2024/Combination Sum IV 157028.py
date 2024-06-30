# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        arr=[]
        memo={}
       
        def dp(sm):
            if sm in memo:
                return memo[sm]
            if sm>target:
                return 0
            if sm==target:
                return 1
            ans=0
            for i in nums:
                ans+=dp(sm+i)

            memo[sm]=ans
            return ans
        print(memo)
        return dp(0)