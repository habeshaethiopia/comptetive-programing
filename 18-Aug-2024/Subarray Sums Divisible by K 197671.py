# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

Python3
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c=0
        dic=defaultdict(int)
        x=0
        dic[x]+=1
        for i in nums:
            x+=i
            if x%k in dic:
                c+=dic[x%k]
            dic[x%k]+=1
        return c