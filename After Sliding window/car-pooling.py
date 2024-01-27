class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        n=max([i[2] for i in trips])
        a=[0]*(n+1)
        for i in trips:
            a[i[1]]+=i[0]
            a[i[2]]-=i[0]
        x=0
        mx=0
        print()
        for i in a:
            x+=i
            mx=max(mx,x)
        return mx<=capacity
