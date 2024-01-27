class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        S=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                if nums[i] +nums[j]+nums[k]==0:
                    if (nums[i] ,nums[j], nums[k]) not in S:
                        S.add((nums[i] ,nums[j], nums[k]))
                        ans.append([nums[i] ,nums[j], nums[k]])
                    k-=1
                    j+=1
                    
                elif nums[i] +nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return ans