from bisect import bisect_left

def merge(left,right):
    l,r=0,0
    ans=[]
    Ol=[i[1] for i in left ]
    Or=[i[1] for i in right ]
    # print(Ol,Or, sep='   *****  ')
    # while l<len(left) and r<len(right):
    #     if Ol[l]>Or[r]:
    #         temp=Or[r]+bisect_left(Ol,Or[r])
    #         ans.append((right[r][0],temp))
    #         r+=1
    #     else:
    #         temp=Ol[l]+bisect_left(Or,Ol[l])
    #         ans.append((left[l][0],temp))
    #         l+=1
        
    while l<len(left):
        temp=Ol[l]+bisect_left(Or,Ol[l])
        ans.append((left[l][0],temp))
        l+=1
    
    while r<len(right):
        temp=Or[r]+bisect_left(Ol,Or[r])
        ans.append((right[r][0],temp))
        r+=1
    # print([i[1] for i in ans])
    return sorted(ans,key=lambda x:x[1])
        



def sort_m(arr,l,r):
    if l==r:
        return [arr[l]]
    mid=(l+r)//2
    left=sort_m(arr,l,mid)
    right=sort_m(arr,mid+1,r)
    # print('left:',left,'right:',right)

    return merge(left,right)



for _ in range(int (input())):
    n=int(input())
    a=list(map(int, input().split()))
    a=[(i,val) for i,val in enumerate(a)]
    new=sort_m(a,0,len(a)-1)
    ans=[0]*len(a)
    for i in new:
        ans[i[0]]=i[1]
    print(*ans)