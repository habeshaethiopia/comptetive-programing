class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        for i,val in enumerate(nums1):
            index = nums2.index(val)
            for x in range(index,len(nums2)):
                if nums2[x]>val:
                    ans[i]=nums2[x]
                    break
        return ans


            