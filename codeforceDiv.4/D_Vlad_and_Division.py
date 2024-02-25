for _ in range(int(input())):
    n = int(input())
    arr=list(map(int, input().split()))
    c=n
    for i in range(n):
        for j in range(i+1,n):
            a=arr[i]
            b=arr[j]
            for l in range(30,1,-1):
                a=a>>l
                b=b>>l
                
                if a!=b:
                    print(a,b,l)
                    break
            else:
                c-=1
    # print(4>>31)     
    print (c)
