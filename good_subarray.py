for _ in range(int(input())):
    n =int(input())
    nums = list(map(int, list(input())))
    pre = [nums[0]]
    for i in range(1,n):
        pre.append(pre[-1] + nums[i])
    mp = {0:1}
    ans = 0
    for i in range(0,n):
        x = pre[i] - i - 1
        ans += mp.get(x,0)
        mp[x] = mp.get(x,0) + 1
 
    print(ans)
