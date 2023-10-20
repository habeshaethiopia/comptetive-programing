import sys

def solve(n, a):
    cnt = 0
    temp = [a[0]]
    for i in range(1, n):
        if a[i] == temp[-1]:
            continue
        else:
            temp.append(a[i])
    if len(temp) == 1:
        return "YES"
    if temp[0] < temp[1]:
        cnt += 1
    if temp[-1] < temp[-2]:
        cnt += 1
    for i in range(1, len(temp) - 1):
        if temp[i - 1] > temp[i] and temp[i] < temp[i + 1]:
            cnt += 1
        if cnt >= 2:
            break
    return "YES" if cnt == 1 else "NO"

if __name__ == "__main__":
    input = sys.stdin.readline
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))