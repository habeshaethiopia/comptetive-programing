for _ in range(int(input())):
    n= int(input())
    arr= list(map(int, input().split()))
    se=set(arr)
    s=sum(arr)

    if s%3==0:
        print(0)
    elif s%3  in se or (s+1)%3==0:
        print(1)
    else:
        for i in arr:
            if i%3==s%3:
                print(1)
                break
        else:
            print (2)
