class NumArray:

    def __init__(self, nums: List[int]):
        self.num=nums
        self.prifx=[0]
        x=0
        for i in nums:
            x+=i
            self.prifx.append(x)
        print(self.prifx)

    def sumRange(self, left: int, right: int) -> int:        
        return self.prifx[right+1]-self.prifx[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)