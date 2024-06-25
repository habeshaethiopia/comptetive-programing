# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = defaultdict(int)
        cnt[0]=1
        pre=0
        ans=0
        for c in word:
            pre=pre^(1<<(ord(c)-ord('a')))
            ans+=cnt[pre] #even pattern
            for i in range(ord('a'),ord('j')+1):
                odd=pre^(1<<(i-ord('a')))
                ans+=cnt[odd]
            cnt[pre]+=1


        return ans

            