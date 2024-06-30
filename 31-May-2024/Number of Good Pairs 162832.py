# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=0
        for i in set(nums):
            c = nums.count(i)
            if c >= 2:
                cnt += ((c)*(c-1))//2
        return cnt