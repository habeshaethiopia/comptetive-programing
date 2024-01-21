class Solution:
    def sortSentence(self, s: str) -> str:
        s= {int(i[-1:]):i[:-1]for i in s.split()}
        ans=['']*len(s)
        for i in range(1,len(ans)+1):
           ans[i-1]=s[i]
        return " ".join(ans)