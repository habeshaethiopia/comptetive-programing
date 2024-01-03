class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        first=0
        second=0
        ans=-1
        while first < len(nums1) and second < len(nums2):
            if nums1[first]<nums2[second]:
                first+=1
            elif nums1[first]>nums2[second]:
                second+=1
            else:
                ans=nums1[first]
                break
        return ans
            