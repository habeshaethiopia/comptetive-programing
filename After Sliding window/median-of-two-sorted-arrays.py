class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        nums1.sort()
        n=len(nums1)
        return float(nums1[(n-1)//2]) if n%2 else (nums1[n//2-1]+nums1[n//2])/2

        