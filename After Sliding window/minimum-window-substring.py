class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = ""
        res_len = len(s) + 1
        tMap, sMap = {}, {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        need = len(tMap)
        l, r, count = 0, 0, 0

        for r in range(len(s)):
            if s[r] in tMap:
                sMap[s[r]] = 1 + sMap.get(s[r], 0)
                if sMap[s[r]] == tMap[s[r]]:
                    count += 1

                    while count == need:
                        if r - l + 1 < res_len:
                            res_len = r - l + 1
                            res = s[l:r + 1]

                        if s[l] in sMap:
                            sMap[s[l]] -= 1

                            if sMap[s[l]] < tMap[s[l]]:
                                count -= 1
                        l += 1
        return res