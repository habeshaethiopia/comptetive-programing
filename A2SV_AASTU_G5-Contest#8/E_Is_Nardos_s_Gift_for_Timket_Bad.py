for _ in range(int(input())):
    n=int(input())
    nums=[int(i) for i in input()]
    dic=[0]
    c=0
    l=1
    for i in nums:
        c+=i
        dic.append(c)
    c=0
    # dic=set(dic)
    for r in range(1,n):
        if r+1 in dic[:r+1]:
            c+=1
        while r>0:
            if r in dic[:r+1]:
                c+=1
                break
            r-=1 
    print(c)
