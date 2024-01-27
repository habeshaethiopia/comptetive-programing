class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        ans=[]
        for i in nums:
            x+=i
            ans.append(x)
        # print(ans)
        for i in range(len(ans)):
            if ans[i]-nums[i]==ans[-1]-ans[i]:
                return i
        return -1