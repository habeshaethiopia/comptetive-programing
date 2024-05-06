n,m=map(int, input().split())

parent = {i:i for i in range(1, n+1) }
MIN = {i:i for i in range(1, n+1) }
MAX = {i:i for i in range(1, n+1) }

parent = {i:i for i in range(1, n+1) }
size = [1] * (n+1)

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parentX = find(x)
    parentY = find(y)
    if parentX != parentY:
        parent[parentX] = parentY
        size[parentY]+=size[parentX]
        MIN[parentY]= min(MIN[parentX],MIN[parentY])
        MAX[parentY]= max(MAX[parentX],MAX[parentY])

for _ in range(m):
    com=input().split()
    if len(com)==3:
        union(int(com[1]), int(com[2]))
    else:
        # print(size,parent)
        node=find(int(com[1]))

        print(MIN[node],MAX[node] ,size[node])

