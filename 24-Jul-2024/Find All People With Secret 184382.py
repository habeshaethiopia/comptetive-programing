# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret=set([0,firstPerson])
        meet={}
        for x,y,t in meetings:
            if t not in meet:
                meet[t]=defaultdict(list)
            meet[t][x].append(y)
            meet[t][y].append(x)
        def dfs(p,met):
            if p in visit:
                return
            secret.add(p)
            visit.add(p)
            for i in met[p]:
                dfs(i,met)
        # print(meet)
        for key in sorted(meet.keys()):
            visit=set()
            for src in meet[key]:
                if src in secret:
                    dfs(src, meet[key])
        return list(secret)
            
            
    