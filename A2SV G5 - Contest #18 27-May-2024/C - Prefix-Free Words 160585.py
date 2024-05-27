# Problem: C - Prefix-Free Words - https://codeforces.com/gym/526229/problem/C

from sys import stdin


class Tirenode:
    def __init__(self):
        self.children=[None for _ in range(2)]
        self.val=None
        self.is_end=False
class tire:
    def __init__(self):
        self.root=Tirenode()
    def insert(self, n):
        dum=self.root
        stack = []
        ans=''
        for i in range(n):
            par=dum
            stack.append(dum)
            if not dum.children[0] or not dum.children[0].is_end:
                if not dum.children[0]:
                    dum.children[0]=Tirenode()
                
                dum=dum.children[0]
                dum.val=0
                ans+='0'
            elif not dum.children[1]or not dum.children[1].is_end:
                if not dum.children[1]:
                    dum.children[1]=Tirenode()
                dum=dum.children[1]
                dum.val=1
                ans+='1'

            else:
                return False
        dum.is_end = True
        while stack and stack[-1].children[1] and stack[-1].children[1].is_end:
            
            x= stack.pop()
            x.is_end=True

            
        return ans
            
    
def rec(r):
    return [(r.val,r.is_end)]+rec(r.children[0])+rec(r.children[1]) if r else []

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    n=int(input())
    a=inlt()

    t=tire()
    pr=[]
    a = sorted((ai, i) for ai, i in zip(a, range(n)))
    pr = [0]*n
    for i, j in a:
        
        r=t.insert(i)
      
        if not r:
            print('NO')
            break
        pr[j] = r
      

    else:
        print('YES')
        print(*pr,sep='\n')

if __name__=='__main__':
    solve()