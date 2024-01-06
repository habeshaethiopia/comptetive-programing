class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mysub=""
        l = 0
        for i in range(len(s)):
            if s[i] in mysub:
                idx = mysub.index(s[i])
                mysub = mysub[idx+1:]
            mysub+=s[i]
            if len(mysub)>l:
                l = len(mysub)
        return l