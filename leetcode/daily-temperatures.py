class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                d=stack.pop()
                ans[d]=i-d
            stack.append(i)
        return ans
        