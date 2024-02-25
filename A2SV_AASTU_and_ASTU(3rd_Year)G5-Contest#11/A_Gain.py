for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    
    s=sorted((nums) )
    ans=[]
    for i in range(n):
        if nums[i]!=s[-1]:
            ans.append(nums[i]- s[-1])
        else:
            ans.append(nums[i]-s[-2])
    print(*ans)