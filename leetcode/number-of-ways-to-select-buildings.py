class Solution:
    def numberOfWays(self, s: str) -> int:
        pri=[]
        x=0
        for i in s:
            x+=int(i)
            pri.append(x)
        suf=[]
        x=0
        for i in s[::-1]:
            x+=int(i)
            suf.append(x)
        ans=0
        # print(len(s), pri[-1])
        zeros=len(s) - pri[-1]
        for i in range(len(s)):
            if s[i]=='0':
                # print('0',pri[i],suf[len(s)-1-i])
                ans+= pri[i]*suf[len(s)-1-i]
            else:
                z=i+1-pri[i]
                # print('1',z,zeros-z)
                ans+= (z)*(zeros-z)
        return ans