class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        both = {fronts[i]:i for i in range(len(fronts)) if fronts[i] ==backs[i]}
        print (both)
        mn = float("inf")
        for i in range(len(fronts)):
            if  fronts[i] not in both:
                if mn >  fronts[i]:
                    mn = fronts[i]
            if backs[i] not in both:
              if mn >  backs[i]:
                    mn = backs[i]
        if mn != float("inf"):
            return mn
        else: 
            return 0
        