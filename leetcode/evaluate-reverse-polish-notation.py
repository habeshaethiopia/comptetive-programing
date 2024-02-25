class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={'+', '-', '*', '/'}
        stack=[]
        for i in tokens:
            if i in op:
                v1=str(stack.pop())
                v2=str(stack.pop())
                print(v1,v2)
                res=eval(v2+str(i)+v1)
                if res>0:
                    res=floor(res)
                else:
                    res=ceil(res)
                print(res)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack.pop())
