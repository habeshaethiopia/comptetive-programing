for _ in range(int (input())):
    n,m=map(int, input().split())
    s=input()
    w=input()
    sens=0
    win=0
    for i in range(m):
        win+=ord(w[i])
        sens+=ord(s[i])
    if sens==win:
            # print(s[i-m:i])
            print('YES')
    else:
        for i in range(m,n):
            sens-=ord(s[i-m])
            sens+=ord(s[i])
            if sens==win:
                # print(s[i-m:i])
                print('YES')
                break
        else:
            print('NO')