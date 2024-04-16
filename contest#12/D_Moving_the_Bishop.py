from sys import stdin


def input():
    return stdin.readline().strip()


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s)])


def invr():
    return map(int, input().split())

from collections import deque

path=[[1,1],[-1,-1],[1,-1],[-1,1]]
def valid(r,c,n,m):
    # print(r,c)
    return r>-1 and c>-1 and r<n and c<m

def bfs(graph, start_node,n,end):
    visited = set()
    queue = deque([start_node])
    ans=0
    while queue:
        for i in range(len(queue)):
            # print(queue)
            r,c,f= queue.popleft()
            visited.add((r,c,f))

            for i,val in enumerate(path):
                pr,pc=val
                row,col=r+pr,c+pc
                # print(*graph,sep='\n')
                if valid(row,col,n,n) and (row,col,i<2) not in visited and graph[row][col]!='#':
                    queue.append((row,col,i<2))
                    if (row,col)==end:
                        return ans

                    
        ans+=1
    return -1

def solve():

    n = int(input())
    ax, ay = inlt()
    bx, by = invr()

    board=[]
    for i in range(n):
        board.append(input())
    print(bfs(board,(ax-1,ay-1,False),n,(bx-1,by-1)))

        


if __name__ == "__main__":
    solve()
