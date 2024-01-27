class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=Counter(nums)
        most =count.most_common()
        print ( list(most[0])[1])
        return list(most[0])[1] > 1
           
