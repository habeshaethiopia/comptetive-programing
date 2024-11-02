from collections import defaultdict
from heapq import heapify, heappop, heappush
from sys import stdin


def input(): return stdin.readline().strip()

N, M = map(int, input().split())
adj = defaultdict(list)

for _ in range(M):
   u, v, w = map(int, input().split())
   u -= 1
   v -= 1
   adj[u].append((v, w))
   adj[v + N].append((u + N, w))
for i in range(N):
   adj[i].append((i + N, 0))

dist = [float('inf')]*(2*N)
visited = [False]*(2*N)
dist[0] = 0
pq = [(0, 0)]
while pq:
   d, v = heappop(pq)
   if visited[v]:
       continue
   visited[v] = True
   for ch, w in adj[v]:
       new_d = d + w
       if new_d < dist[ch]:
           dist[ch] = new_d
           heappush(pq, (new_d, ch))

for i in range(N + 1, 2*N):
   if dist[i] == float('inf'):
       print("-1", end=" ")
   else:
       print(dist[i], end=" ")