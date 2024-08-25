# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        sum, step=0,0
        target=abs(target)
        while sum<target:
            sum+=step
            step+=1
        while (sum-target)%2==1:
            sum+=step
            step+=1
        return step-1