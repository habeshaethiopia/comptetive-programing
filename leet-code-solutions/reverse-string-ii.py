class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        newstr=""
        f=True
        inc=k
        for i in range(0,len(s),k):
            if f:
               newstr+=s[i:k][::-1]
               f = False
            else:
                newstr +=s[i:k]
                f=True
            k+=inc
        return newstr