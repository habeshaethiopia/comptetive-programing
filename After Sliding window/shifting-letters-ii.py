class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        a=[0]*(n+1)
        for i in shifts:
            if i[2]==0:
                a[i[0]]+=-1
                a[i[1]+1]+=1
            else:
                a[i[0]]+=1
                a[i[1]+1]-=1
        ans=[]
        x=0
        for i in a:
            x+=i
            ans.append(x)

        for i in range(n):
            ans[i]=chr((ord(s[i])+ans[i]-97)%26 + 97)
        return "".join(ans[:n])

            