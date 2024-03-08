class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""

        def dicConc(start, end):
            nonlocal ans
            myset = set([s[i] for i in range(start, end)])
            flag = True
            br = 0
            for i in range(start, end):
                if s[i].isupper():
                    if s[i].lower() in myset:
                        pass
                    else:
                        flag = False
                        br = i
                        break
                else:
                    if s[i].upper() in myset:
                        pass
                    else:
                        flag = False
                        br = i
                        break
            if flag:
                if len(ans) < len(s[start:end]):
                    ans = s[start:end]
            else:
                dicConc(start, br)
                dicConc(br + 1, end)

        dicConc(0, len(s))
        return ans
