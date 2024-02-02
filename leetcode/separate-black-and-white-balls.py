class Solution:
    def minimumSteps(self, s: str) -> int:
        a=[0]*(len(s)+1)
        c=0
        for i in range(len(s)):
            if s[i]=='0':
                a[i]+=c
            else:
                c+=1 
        return sum(a)