class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        mydic = {}
        c = 0
        for i in range(len(s)):
            if s[i] == "|":
                mydic[i] = c
            else:
                c += 1
        if not mydic:
            return [0] * len(queries)
        ans = []
        candles = [i for i in mydic]
        print(candles)
        for i in queries:
            idx = bisect_left(candles, i[0])
            left = candles[idx] if idx < len(candles) else candles[-1]

            idxr = bisect_right(candles, i[1]) - 1
            right = candles[idxr] if idxr >= 0 else candles[0]

            plates = mydic[right] - mydic[left]
            if plates > 0:
                ans.append(plates)
            else:
                ans.append(0)
        return ans
