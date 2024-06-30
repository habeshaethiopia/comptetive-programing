# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l=0
        r=position[-1]
        ans=-1
        while l<=r:
            mid=(l+r)//2
            prev=position[0]
            num=1
            for i in range(1, len(position)):
                if position[i]-prev>=mid:
                    prev=position[i]
                    num+=1
            if num>=m:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
