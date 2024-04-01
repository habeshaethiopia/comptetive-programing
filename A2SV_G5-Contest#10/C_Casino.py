from math import lcm
n=int(input())
arr= list(map(int, input().split()))
x=1
for i in arr:
    x=lcm(x,i)
for i in arr:
    gc=x//i
    d=2
    myset=set()
    while d*d<=gc:
        if gc%d:
            d+=1
        else:
            gc//=d
            myset.add(d)
    myset.add(gc)
    if 1 in myset:
       myset.remove(1) 
    if 2 in myset:
        myset.remove(2)
    if 3 in myset:
        myset.remove(3)
    if myset:
        print('No')
        break
else:
    print('Yes')
