class Solution:
    def romanToInt(self, s: str) -> int:
        symbol={"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        val = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and symbol[s[i]] < symbol[s[i + 1]]:
                val += symbol[s[i + 1]] - symbol[s[i]]
                i += 2
            else:
                val += symbol[s[i]]
                i += 1
        return(val)
        