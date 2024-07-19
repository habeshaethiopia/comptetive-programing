# Problem: D - Heap Operations - https://codeforces.com/gym/535309/problem/D

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr=[1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        return sum(arr[:k])