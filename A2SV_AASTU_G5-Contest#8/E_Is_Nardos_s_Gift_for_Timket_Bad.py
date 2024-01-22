for _ in range(int(input())):
    n=int(input())
    nums=[int(i) for i in input()]
    dic={1:1}
    c=0
    ans=0
    for i,val in enumerate(nums):
        c+=val
        if c-i in dic:
            ans+=dic[c-i]
            dic[c-i]+=1
        else:
            dic[c-i]=1
       
    print(ans)
