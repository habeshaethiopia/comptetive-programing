class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle=[]
        n2=n
        for i in range(n):
            shuffle.append(nums[i])
            shuffle.append(nums[n2])
            n2 += 1
        return shuffle
            