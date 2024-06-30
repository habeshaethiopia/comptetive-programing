# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp=defaultdict(int)
        mx=0
        for i in range(len(arr)-1,-1,-1):
            dp[arr[i]]=max(dp[arr[i]],dp[arr[i]+difference]+1)
            mx=max(mx, dp[arr[i]])
        print(dp)
        return mx


