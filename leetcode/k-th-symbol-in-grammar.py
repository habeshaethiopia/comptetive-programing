class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        '''
        def rec(n,k):
            ans=[]
            if n==0:
                return '0'
            curr=rec(n-1,k)
            if len(curr)>k:
                return curr
            for i in curr:
                if i=='0':
                    ans.append('01')
                else:
                    ans.append('10')
            return ''.join(ans)
        s=rec(n,k)
        return int(s[k-1])'''
        def cur(n,k):
            if n==1:
                return 0
            val=2**(n-2)
            if val>=k:
                return cur(n-1,k)
            else:
                print(k-val)
                return 1+cur(n-1,k-val)
        s=cur(n,k)
        print(s)
        return 1 if s%2 else 0