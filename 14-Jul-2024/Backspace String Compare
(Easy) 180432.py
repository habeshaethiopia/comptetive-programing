# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def afterbackspace(s):
            ns=''
            c=0
            l=len(s)-1
            while l>-1 :
                if s[l]=='#':
                    c+=1
                else:
                    if c==0:
                        ns+=s[l]
                    else:
                        c-=1
                l-=1
            return ns
        return afterbackspace(s)==afterbackspace(t)
