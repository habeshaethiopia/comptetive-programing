for _ in range(int(input())):
    a,b,l= map(int, input().split())
    ans=0
    k=set()
    def rec(ab,lm):
        if l==0 or l%a:
            return 0
        k.add(l//a)
        k.add(a)
        k.add(l)
        return 1+ rec(a,l//a)
    an=rec(a,l)
    bn=rec(b,l)
    for i in range(an+1):
        for j in range(bn+1):
            ans=rec((a**i)*(b**j),l)
            print(s)

    print(len(k))
    