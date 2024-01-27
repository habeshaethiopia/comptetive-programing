class Solution:
    def printVertically(self, s: str) -> List[str]:
        li=s.split()
        res=[]
        n = max([len(i) for i in li])
        s=[words+" " *(n-len(words)) for words in li]
        for i in range(n):
            temp=""
            for y in s:
                if y[i]:
                    temp+=y[i]
                else:
                    temp += " "
            res.append(temp.rstrip())
        return res


