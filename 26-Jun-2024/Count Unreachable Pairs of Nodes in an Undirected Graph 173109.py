# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # Naive implementation of union()
        def Union(x, y):

            xset = find(x)
            yset = find(y)
            cost = 0
            if xset == yset:
                return 0
            if size[xset] > size[yset]:
                parent[yset] = xset
                cost = size[yset] * size[xset]
                size[xset] += size[yset]
                size[yset] -= size[yset]

            else:
                parent[xset] = yset
                cost = size[yset] * size[xset]
                size[yset] += size[xset]
                size[xset] -= size[xset]
            return cost

        for x, y in edges:
            Union(x, y)
        
        for i in range(n):
            parent[i] = find(i)
        
        cnt = defaultdict(int)
        for i in range(n):
            cnt[parent[i]] += 1
        ans=0
        print(size)
        for i in cnt:
            ans+=Union(0,i)

        return ans
