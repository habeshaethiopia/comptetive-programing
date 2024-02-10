class Solution:
    def bestClosingTime(self, customers: str) -> int:
        a=[0]*len(customers)+[0]
        N=[0]*len(customers)+[0]
        for i in range(len(a)-1):
            if customers[i]=='Y':
                a[i]=1
            else:
                N[i]=1
        ans=[]
        x=0
        n=0
        no=[]
        for i in range(len(a)):
            x+=a[len(a)-1-i]
            ans.append(x)
            no.append(n)
            n+=N[i]
        ans=ans[::-1]
        print(ans,no)

        for i in range(len(a)):
            ans[i]+=no[i]
        return ans.index(min(ans))