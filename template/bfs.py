from collections import deque


def valid(r,c):
    #path=[[1,0],[0,1],[-1,0],[0,-1]]
    return r>-1 and c>-1 and r<len(grid) and c<len(grid[0])

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
