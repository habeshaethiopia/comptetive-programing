class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        temp = []

        def com(curr):
            if len(temp) == k and sum(temp) == n:
                ans.append(temp[:])
                return
            if len(temp) > k:
                return
            for i in range(curr, 10):
                if sum(temp)>n:
                    continue
                temp.append(i)
                com(i + 1)
                temp.pop()

        com(1)
        return ans
