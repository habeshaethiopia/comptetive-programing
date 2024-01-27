class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count = 0
        # check for the odd situation
        for i in range(len(nums)-1):
            # check for any situation(increasing situation)
            if nums[i]>nums[i+1]:
                count +=1
                # handling the test cases like [3,4,2,3] must be false
                if i>0 and nums[i-1]> nums[i+1]:
                    nums[i+1]=nums[i]

        if count > 1:
            return False
        else:
            return True
            