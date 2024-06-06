# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = [0] * (len(s) + 1)
        c = 0

        for i in range(len(s)):
            if s[i] == "0":
                ans[i] += c
            else:
                c += 1
        return sum(ans)
