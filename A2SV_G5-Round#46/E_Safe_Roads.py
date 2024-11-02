from collections import deque, defaultdict

def solve():
    n, m = map(int, input().split())
    g = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    que = deque([1])
    vis = [-1] * (n + 1)
    visr = [-1] * (n + 1)
    ways = [0] * (n + 1)
    waysr = [0] * (n + 1)
    
    vis[1] = 0
    ways[1] = 1
    dis = 1
    
    while que:
        cur_s = len(que)
        for _ in range(cur_s):
            node = que.popleft()
            for child in g[node]:
                if vis[child] == -1:
                    que.append(child)
                    vis[child] = dis
                    ways[child] = ways[node]
                elif dis == vis[child]:
                    ways[child] += ways[node]
        dis += 1

    que.append(n)
    dis = 1
    visr[n] = 0
    waysr[n] = 1
    
    while que:
        cur_s = len(que)
        for _ in range(cur_s):
            node = que.popleft()
            for child in g[node]:
                if visr[child] == -1:
                    que.append(child)
                    visr[child] = dis
                    waysr[child] = waysr[node]
                elif dis == visr[child]:
                    waysr[child] += waysr[node]
        dis += 1
    
    ans = 1.0
    div = vis[n]
    
    for i in range(2, n):
        cur_total = 0
        for child in g[i]:
            if vis[i] + visr[child] + 1 == vis[n]:
                cur_total += ways[i] * waysr[child]
        
        ans = max(ans, (cur_total / ways[n]) * 2)
    
    print(ans)

if __name__ == "__main__":
    solve()