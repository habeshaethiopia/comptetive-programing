# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        memo = nums[:]

        def mod(n):
            a = ""
            for i in str(n):
                a += str(mapping[int(i)])
            return int(a)

        for i in range(len(nums)):
            nums[i] = mod(nums[i])
        mim=[ [memo[i],nums[i] ] for i in range(len(nums))]
        mim.sort(key=lambda x: x[1])
        return [i[0] for i in mim]
