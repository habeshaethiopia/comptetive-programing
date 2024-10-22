# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        mxc=0
        temp=0
        for i in nums:
            if i == mx:
                temp+=1
            else:
                mxc=max(temp,mxc)
                temp=0
        mxc=max(temp,mxc)
        
        return mxc