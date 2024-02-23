class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        mono=deque()
        ans=[]
        r=0  
        for l in range(len(nums)-k+1):
            while r-l+1<=k:
                while mono and mono[-1]<nums[r]:
                    mono.pop()
                mono.append(nums[r])
                # print(r,l)
                r+=1
            # print(mono)
            ans.append(mono[0])
            if nums[l]==mono[0]:
                mono.popleft()
        return ans