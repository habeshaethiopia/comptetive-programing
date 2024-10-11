# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        for i in range(len(edges)):
            edges[i].append(succProb[i])
       
        prev = [0] * n
        prev[start_node] = 1
        
        
        # Perform N-1 iterations (where N is the number of nodes)
      
        for i in range(n):
            
            curr = prev[:]
            # Relax all edges
            for u, v, w in edges:
                curr[v] =max(prev[u]*w, curr[v]) 
                curr[u] =max(prev[v]*w, curr[u]) 
                  
                # print(curr[v], u,v,w)
            if curr == prev:
                break
            prev = curr[:]
        ans=prev[end_node]
        # print(prev, edges)
        return ans