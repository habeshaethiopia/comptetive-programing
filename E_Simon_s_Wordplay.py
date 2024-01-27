for _ in range(int(input())):
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())
    
    #    a,b,c,d,e
    ans=[]
    for i in ['a','b','c','d','e']:
        mylist=[]
        for l in s:
            n=2*l.count(i)-len(l)
            mylist.append(n)
        mylist.sort(reverse=True)
        Sum=0
        c=0
        for x in mylist:
            Sum+=x
            if Sum<=0:
                break
            c+=1
        ans.append(c)
    print(max(ans))
            


