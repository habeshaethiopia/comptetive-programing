class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        ans=0
        for i in range(len(height)):
            # print(stack)
            while stack and height[stack[-1]] <= height[i]:
                p=stack.pop()
                if stack:
                    # finding the area using monotonic stack decreasing
                    h=min(height[stack[-1]],height[i])-height[p]
                    w=i-stack[-1]-1
                    # print(h,w)
                    ans+=h*w
            stack.append(i)
        return ans
