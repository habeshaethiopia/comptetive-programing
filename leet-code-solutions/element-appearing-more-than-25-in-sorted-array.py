class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        num = Counter(arr).most_common()
        return list(num[0])[0]