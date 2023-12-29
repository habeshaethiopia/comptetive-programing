class Solution:
    def smallestNumber(self, num: int) -> int:
        _ve=False
        ans=""
        if num < 0:
            _ve=True
            
            num=[i for i in str(num)[1:]]
            while num:
                mn=max(num)
                ans+=mn
                num.remove(mn)
            return -int(ans)
        else:
            n0=str(num).count('0')
            num=[i for i in str(num) if i != '0']

            if num:
                while num:
                    mn=min(num)
                    ans+=mn
                    num.remove(mn)
                ans=ans[0]+'0'*n0 + ans[1:]
            else:
                return 0
            return int(ans)
