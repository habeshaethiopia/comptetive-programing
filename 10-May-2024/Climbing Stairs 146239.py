# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.mem={0:1}
    def climbStairs(self, n: int) -> int:
        if n==1:
            self.mem[1]=1
            return 1
        if n not in self.mem:
            self.mem[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.mem[n]

        