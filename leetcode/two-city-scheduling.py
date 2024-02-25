class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ''' 
            sorting them in their gap with out abs 
            so the first half is go to city A
            and the second half go to city B
        '''
        costs.sort(key=lambda x:x[0]-x[1])
        n=len(costs)
        ans=0
        for i in range(n//2):
            ans+=costs[i][0]
            ans+=costs[i+n//2][1]
        return ans