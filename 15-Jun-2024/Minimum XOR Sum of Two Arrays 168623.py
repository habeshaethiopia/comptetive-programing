# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0
            mn = sys.maxsize
            for j in range(n):
                if mask & (1 << j) == 0:
                    mn = min(mn, (nums1[i] ^ nums2[j]) + dp(i + 1, mask | (1 << j)))
            return mn

        n = len(nums1)
        return dp(0, 0)
