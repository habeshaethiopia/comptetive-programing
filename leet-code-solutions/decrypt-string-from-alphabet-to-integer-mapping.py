class Solution:
    def freqAlphabets(self, s: str) -> str:
        sym="0abcdefghijklmnopqrstuvwxyz"
        st=""
        n = len(s)-1
        while n>=0:
            if s[n]=='#':
                st= sym[int(s[n-2:n])] + st
                n -=3
                print(st)
            else:
                st = sym[int(s[n])] + st
                print(st)
                n-=1

        return st
                
