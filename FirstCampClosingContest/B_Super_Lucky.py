n=int(input())
ans=4444477777


def backtrack(val, n_4,n_7):
    global ans
    if val>ans:
        return 
    
    if val>=n and n_4==n_7:
        ans=min(ans,val)
        return
    backtrack(val*10+4,n_4+1,n_7)
    backtrack(val*10+7,n_4,n_7+1)
    
backtrack(0,0,0)
print(ans)
