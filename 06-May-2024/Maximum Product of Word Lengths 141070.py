# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def convert_to_bit(word):
            result = 0
            for l in word:
                result |= 1 << (ord(l) - ord("a"))
            return result

        length = [len(i) for i in words]
        bit = [convert_to_bit(i) for i in words]
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not bit[i] & bit[j]:
                    ans = max(ans, length[i] * length[j])
        return ans
