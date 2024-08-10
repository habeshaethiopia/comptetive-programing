# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter([i for i in word])
        print(c)
        keys=sorted(c.keys(), key=lambda x:c[x], reverse=True)
        ans=0
        for i in range(len(keys)):
            ans+= c[keys[i]]*ceil((i+1)/8)
        return ans