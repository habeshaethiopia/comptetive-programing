class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        a=[0]*(len(nums)+1)
        for i in requests:
            a[i[0]]+=1
            a[i[1]+1]-=1
        x=0
        ans=[]
        for i in a:
            x+=i
            ans.append(x)
        ans=ans[:-1]
        ans.sort()
        nums.sort()
        print(ans,nums,sep='\n')
        n=0
        for i in range(len(nums)):
            n+=ans[i]*nums[i]

        return n%(10**9 + 7)

        

        
