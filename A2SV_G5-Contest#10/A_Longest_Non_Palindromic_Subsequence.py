for _ in range(int(input())):
    s=input()
    myset=set(s)
    print(-1 if len(myset)==1 else len(s)-1)
