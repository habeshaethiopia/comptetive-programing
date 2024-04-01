class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        a=set()
        path=[]
        
        candidates.sort()
        def back(curr):
            if sum(path)==target and tuple(path) not in a:

                ans.append(path[:])
                a.add(tuple(path[:]))
                return
            elif sum(path)>target:
                return
            k=float(inf)
            for i in range(curr,len(candidates)):
                if k==candidates[i]:
                    continue
                path.append(candidates[i])

                back(i+1)
                k=path.pop()

        print(len(candidates))
        if sum(candidates)>=target:
            back(0)
        
        return ans