class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def com(curr,temp):
            if len(temp)==k:
                ans.append(temp[:])
                return
            if curr>n:
                return
            # for i in range(curr,n+1):
            temp.append(curr)
            com(curr+1,temp)
            temp.pop()
            com(curr+1,temp)
        com(1,[])
        return ans