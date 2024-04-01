for _ in range(int(input())):
    n,d = map(int, input().split())
    arr= [i for i in input()]
    ans=[]
    d=str(d)
    for i in arr:
        if i>=d:
            ans.append(i)
        else:
            ans.append(d)
            ans.extend(arr[len(ans)-1:])
            break
    else:
        ans.append(d)
    print(''.join(ans))