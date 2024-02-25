class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt=Counter(s)
        stack=[]
        for i in s:
            if i not in stack:
                while stack and stack[-1] >=i and cnt[stack[-1]]>1:
                    cnt[stack[-1]]-=1
                    stack.pop()
                
                stack.append(i)
            else:
                cnt[i]-=1
            
            print(stack)
        temp=set()
        ans=''
        for i in stack:
            if i not in temp:
                temp.add(i)
                ans+=i

            if not temp:
                temp.add(i)
            
        return ans


            