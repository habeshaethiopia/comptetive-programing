class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vol = set(['a', 'e', 'i', 'o', 'u'])
        mx = 0
        c = 0
        for i in range(k):
            if s[i] in vol:
                c += 1
        mx = c
        for i in range(k, len(s)):
            if s[i] in vol:
                c += 1
            if s[i - k] in vol:
                c -= 1
            mx = max(c, mx)
        return mx