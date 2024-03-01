class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def cal(l,r, t):
            #checking both sides recursively
            if t:
                if l==r:
                    print(l)
                    return nums[l]
                left=cal(l+1,r, not t)+nums[l]
                right=cal(l,r-1, not t)+nums[r]
                return max(right, left)
            else:
                if l==r:
                    return -nums[l]
                left=cal(l+1,r, not t)-nums[l]
                right=cal(l,r-1, not t)-nums[r]
                return min(right, left)
        ans=cal(0,len(nums)-1, True)
        return ans>=0



