class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic={}
        ans=[0]*len(nums)
        # for left side
        for i in range(len(nums)):
            if nums[i] in dic:
               temp=dic[nums[i]]
               ans[i]+=(i-temp[0])*temp[1]+ans[temp[0]]
               dic[nums[i]]=[i, temp[1]+1]
            else:
                dic[nums[i]]=[i,1]
        print(ans)
        dic={}
        ansr=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in dic:
               temp=dic[nums[i]]
               ansr[i]+=abs(i-temp[0])*temp[1]+ansr[temp[0]]
               dic[nums[i]]=[i, temp[1]+1]
            else:
                dic[nums[i]]=[i,1]
        ans=[ans[i]+ansr[i] for i in range(len(nums))]
        return ans