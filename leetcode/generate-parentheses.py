class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        temp=[]
        def back(c,o):
            # print(temp)
            if len(temp)==2*n and c==o:
                ans.append(''.join(temp))
                return
            if o<n:
                temp.append('(')
                back(c,o+1)
                temp.pop()
            if o>c and c<n:
                temp.append(')')
                back(c+1,o)
                temp.pop()
        back(0,0)
        return ans