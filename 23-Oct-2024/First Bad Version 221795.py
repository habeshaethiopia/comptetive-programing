# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        h=n
        ans=n
        while h>=l:
            mid =(l+h)//2
            if isBadVersion(mid):
                ans=min(ans,mid)
                h=mid-1
            else:
                l=mid+1
        return ans