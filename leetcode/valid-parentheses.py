class Solution:
    def isValid(self, s: str) -> bool:
        y={')':'(', ']':'[', '}':'{'}
        z=[')','}',']']

        stack=[]
        for i in s:
            if i in y.values():
                stack.append(i)
            elif i in z:
                if len(stack) and stack[-1]== y[i]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

