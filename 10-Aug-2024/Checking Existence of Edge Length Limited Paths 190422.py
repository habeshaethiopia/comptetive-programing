# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key= lambda x:x[2])
        new =[queries[i]+[i] for i in range(len(queries))]
        new.sort(key= lambda x:x[2])
        parent = {i:i for i in range(n) }
        size = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]
        ans=[False]*len(new)
        last=0
        for q in new:
            for i in range(last,len(edgeList)):
                u,v,w=edgeList[i]
                last=i
                if w<q[2]:
                    union(u,v)
                else:
                    break
            ans[q[3]]=find(q[0])==find(q[1])
        return ans
