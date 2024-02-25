for _ in range(int(input())):
    s=input()
    ans=[s[:(len(s)//2)+1]]
    half=s[(len(s)//2)+1:]
    x=""
    for i in range(len(half)):
        if ans[0][i] != half[i]:
            x+=ans[0][i]
    print(*ans ,x)
    