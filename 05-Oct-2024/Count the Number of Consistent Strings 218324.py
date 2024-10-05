# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow=set([i for i in allowed])
        ans=0
        for w in words:
            for l in w:
                if l in allow:
                    pass
                else:
                    break
            else:
                ans+=1
        return ans