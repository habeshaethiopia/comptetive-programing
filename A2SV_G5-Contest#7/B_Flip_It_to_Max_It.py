for _ in range(int(input())):
    n=int(input())
    num=list(map(int,input().split()))
    new=[]
    for i in range(len(num)):
        if num[i]>0 or num[i] <0:
            new.append(num[i])
    n=len(new)
    c=1 if n>0 and new[0]<0 else 0
    l=0
    ans=0
    if n>0:
        ans=abs(new[0])
    left=0
   
    for i in range(1,n):
        ans+=abs(new[i])
        if new[i-1]>0 and new[i]<0 :
            c+=1
    # print(new)
            
    print (ans,c)