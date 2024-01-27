for _ in range(int(input())):
    r, c = map(int, input().split())
    mtx = []
    swap = set()
    for i in range(r):
        mtx.append(list(map(int, input().split())))
    for i in range(r):
        sor = sorted(mtx[i])
        
        for j in range(c):
            if mtx[i][j] != sor[j]:
                swap.add(j + 1)
    # print(swap)         
    for i in range(r):
        br = False
        sor = sorted(mtx[i])
        
        if len(swap) == 2:
            t = list(swap)
            mtx[i][t[0] - 1], mtx[i][t[1] - 1] = mtx[i][t[1] - 1], mtx[i][t[0] - 1]
        for j in range(c):
                if mtx[i][j] != sor[j]:
                        print(-1)
                        br = True
                        break
        if br:
            break
    else:
        if len(swap) == 2:
            print(*list(swap))
        elif len(swap) == 0:
            print(*[1, 1])
        elif len(swap) > 2:
            print(-1)
