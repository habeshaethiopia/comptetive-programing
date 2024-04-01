n,k = map(int, input().split())
acc=list(map(int, input().split()))
left=0
right=max(acc)
while right>=left:
    mid=(right+left)/2
    r=0
    l=0
    for i in acc:
        if i<mid:
            l+=mid-i
        else:
            r+=(i-mid)*(1-k/100)
    if r>=l:
        left=mid+10e-7
    else:
        right=mid-10e-7
print(mid)