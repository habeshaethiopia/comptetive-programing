
for i in range(int(input())):
    n=int (input())
    s = list(map(int,input().split()))
    n1=""
    n2=""
    n=list(set(s))

    if s.count(n[1])>s.count(n[0]):
        print(s.index(n[0])+1)
    else:
        print(s.index(n[1])+1)

