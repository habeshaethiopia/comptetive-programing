# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cnt=Counter(nums)
        arr=list(cnt.keys())
    
        def quick_sort(nums,left,right):
            if left>=right :
                return
            
            idx=partition(nums,left,right)
            quick_sort(nums,left,idx-1)
            quick_sort(nums,idx+1, right)
    
        def partition(nums,left,right):
            
            p=left
            l=p+1
            r=p+1

            while r<=right:
                if nums[p]>nums[r]:
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                r+=1
            l=l-1
            nums[p],nums[l]=nums[l],nums[p]
            return l
        quick_sort(arr,0,len(arr)-1)
        num=[]
        for i in arr:
            num.extend([i]*cnt[i])
        return num[-k]
