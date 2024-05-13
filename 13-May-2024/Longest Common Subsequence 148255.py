# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(l1,l2):
            if l1==len(text1) or l2==len(text2):
                return 0
            if text1[l1]==text2[l2]:
                return dp(l1+1,l2+1)+1
            else:
                r1=dp(l1+1,l2)
                r2=dp(l1,l2+1)
                return max(r1,r2)
        return dp(0,0)

