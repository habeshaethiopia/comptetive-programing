# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(2,n,1000000007)+1000000005)%1000000007