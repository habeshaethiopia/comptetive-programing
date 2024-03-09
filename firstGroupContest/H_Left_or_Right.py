for _ in range(int(input())):
    n=int(input())
    s=input()
    l=0
    r=n-1
    pri=0
    ans={}
    for i in range(n):
        if s[i] =='R':
            pri+=n-i-1
        else:
            pri+=i
    k=0
    while l<r:
        if s[l]=='R' and s[r]=='L':
            l+=1
            r-=1
        elif s[l]=='L' and s[r]=='L':
            l+=1
            r-=1
            k+=1
            up=n-l-1-l
            ans[k]=up if up>0 else 0
        elif s[l]=='L' and s[r]=='R':
            k+=1
            if l< n-r:
                l+=1
                up=n-l-1-l
            else:
                r-=1
                up=l-n-r-1
            ans[k]=up if up>0 else 0
        elif s[l]=='R' and s[r]=='R':
            r-=1
            k+=1
            up=r-n-r-1
            ans[k]=up if up>0 else 0
    an=[]
    for i in ans:
        an.append(pri+ans[i])
    print(ans)
    print(*an)



            


