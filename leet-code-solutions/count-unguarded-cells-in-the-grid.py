class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded=set()
        wall=set([(i[0],i[1]) for i in walls])
        g=set([(i[0],i[1]) for i in guards])
        for guard in guards:
            wallfound1=False
            wallfound2=False
            a=1
            b=-1
            for i in range(m-1):
                up=(guard[0]+b,guard[1])
                down=(guard[0]+a,guard[1])
                # print(up, down, i)
                if not wallfound1 and up[0]>=0:
                    if up not in  guarded and up not in wall and up not in g:
                        guarded.add(up)
                    elif up in wall or up in g:
                        wallfound1=True
                    b-=1
                if not wallfound2 and down[0]<m:
                    # print("get")
                    if down not in  guarded and down not in wall and down not in g:
                        guarded.add(down)
                    elif down in wall or down in g:
                        wallfound2=True
                    a+=1
                if wallfound1 and wallfound2:
                    break
            wallfound1=False
            wallfound2=False

            l=-1
            r=1
            for i in range(n-1):
                right=(guard[0],guard[1]+r)
                left=(guard[0],guard[1]+l)
                # print("right, left", right, left, i)
                if not wallfound1 and left[1]>=0:
                    if left not in  guarded and left not in wall  and left  not in g:
                        guarded.add(left)
                    elif left  in  wall or left  in g:
                        wallfound1=True
                    l-=1
                if not wallfound2 and right[1]<n:
                    if right not in  guarded and right not in wall and right not in g:
                        guarded.add(right)
                    elif right in wall or right in g:
                        wallfound2=True
                    r+=1
                if wallfound1 and wallfound2:
                    break
        print(guarded)
        return m*n - len(guards)-len(walls)-len(guarded)
    