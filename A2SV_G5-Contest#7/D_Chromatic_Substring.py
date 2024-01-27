for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ch = ["R", "G", "B"]
    ans = float("inf")
    for i in range(3):
        c = 0
        x = 0
        flip = set()
        for j in range(n):
            if c < k:
                if s[j] != ch[(j + i) % 3]:
                    x += 1
                    flip.add(j)
                c += 1
            else:
                ans = min(x, ans)
                if j - k in flip:
                    x -= 1
                    flip.remove(j - k)
                if s[j] != ch[(j + i) % 3]:
                    x += 1
                    flip.add(j)
        else:
           ans = min(x, ans) 
    print(ans)
