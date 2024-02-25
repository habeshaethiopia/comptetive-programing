class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[""]
        for i in path.split('/'):
            if i not in ['..','.',""]:
                stack.append(i)
            if len(stack)>1 and i =='..':
                stack.pop()
        path= '/'.join(stack)
        return path if path else '/'

