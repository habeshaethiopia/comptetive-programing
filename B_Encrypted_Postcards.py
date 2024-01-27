for _ in range(int (input())):
    n=int(input())
    s=input()
    ans=s[0]
    i=1
    while i  < n:
        for j in range(i,n):
            if ans[-1]==s[j]:
                
                if j+1<n:
                    ans+=s[j+1]
                    i=j+1
                break
        i+=1
    print(ans)