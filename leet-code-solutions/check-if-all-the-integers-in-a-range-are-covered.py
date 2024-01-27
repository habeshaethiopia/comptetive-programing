class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        lis = set(range(left, right+1))
        num=set()
        for i in ranges:
            num.update(range(i[0],i[1]+1))
        if lis.issubset(num):
            return True
        return False