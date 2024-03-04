class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def com(curr,temp):
            if len(temp)==k:
                ans.append(temp[:])
                return
        
            for i in range(curr,n+1):
                temp.append(i)
                com(i+1,temp)
                temp.pop()
        com(1,[])
        return ans