# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        ind=defaultdict(int)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            ind[a]+=1
            ind[b]+=1
        
        q=deque([i for i in range(n) if ind[i]==1])
        
        ans=[]
        # print(q, ind)
        while q:
            ans=[]
            for _ in range(len(q)):
                x=q.popleft()
                ans.append(x)
                for i in g[x]:
                    ind[i]-=1
                    if ind[i]==1:
                        q.append(i)
            # print(ans)
        return ans if ans else [0]


