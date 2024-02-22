class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        x=0
        stack=[0]
        for i in s:
            if i=='(':
                stack.append(0)
            else:
                x=stack.pop()
                if x==0:
                   stack[-1]+=1
                else:
                    stack[-1]+=x*2
        return stack[-1]
            
        