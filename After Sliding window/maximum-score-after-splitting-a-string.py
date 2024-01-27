class Solution:
    def maxScore(self, s: str) -> int:
        o=0
        c=0
        sm=sum([int(i) for i in s])
        ans=0
        az=0
        ao=0
        for i in range(len(s)-1):
            if s[i]=='0':
                o+=1
            else:
                c+=1

            az=o
            ao=sm-c
            ans=max(ans,az+ao)
        return ans            