class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sq = lambda x: x**2
        for i in range(min(n,20)):
            n = str(n)
            print sq(20)
            li=map(int,list(n))
            n = sum(map(sq,li))
            if n == 1:
                return True
           
        else:
            print(n)
            return False 