from sys import stdin


def input():
    return stdin.readline().strip()


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def solve():
    n = int(input())
    a = inlt()
    q = int(input())
    prev = []
    x = [0] * 31
    for i in range(n):
        bit = bin(a[i])[2:]
        bit = "0" * (31 - len(bit)) + bit
        for i in range(31):
            if bit[i] == "1":
                x[i] += 1
        prev.append(x[:])

    ans = []
    # print(prev)
    for _ in range(q):
        l, k = invr()
        r = n-1
        l=l-1
        start=l
        temp=-1
        if a[l] >= k:
            while l <=r:
                
                mid = (l + r) // 2
                win = mid - start + 1
                mybit = prev[mid]

                left = prev[start-1] if start-1 >=0 else [0]*31
                val = ""
                for i in range(31):
                    if mybit[i] - left[i] == win:
                        val += "1"
                    else:
                        val += "0"
                val = int(val, 2)
                # print(a[l],'-',a[mid],'=',val)
                if val >= k:
                    temp=mid
                    l = mid + 1
                else:
                    r = mid - 1
            ans.append(temp+1)
        else:
            ans.append(-1)
        # print('break', ans[-1])
    print(*ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
