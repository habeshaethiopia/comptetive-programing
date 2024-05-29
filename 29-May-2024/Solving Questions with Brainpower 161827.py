# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # @cache
        # def dp(i):
        #     if i>=len(questions):
        #         return 0
        #     l=dp(i+1)
        #     t=dp(i+1+questions[i][1]) + questions[i][0]
        #     return max(l,t)
        # # return dp(0)
        '''botom up'''
        dp=[0]*len(questions)
        n=len(questions)
        check=lambda x: dp[x] if x<n else 0
        for i in range(n-1,-1,-1):
            dp[i]=max(check(i+1+questions[i][1])+questions[i][0],check(i+1))
        return dp[0]