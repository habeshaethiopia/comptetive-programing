class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners= {i[0] for i in matches }
        losers= {i[1] for i in matches }
        count={}
        for i in matches:
            count[i[1]]=count.get(i[1],0)+1
        loss=[i[1] for i in matches ]

        res=[list(winners-losers),[ i for i in count if count[i]==1]]
        res[1].sort()
        res[0].sort()   
        return res