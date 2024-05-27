# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

from sys import stdin
class Tirenode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end=False
        self.n=0
class tire:
    def __init__(self):
        self.root=Tirenode()
    def insert(self, s:str)->None:
        dum=self.root
        for i in s:
            idx=ord(i)-ord('a')
            if not dum.children[idx]:
                dum.children[idx]=Tirenode()
            dum=dum.children[idx]
            dum.n+=1
    def search(self, s):
        dum=self.root
        ret=0
        for i in s:
            idx=ord(i)-ord('a')
            if not dum.children[idx]:
                break
            dum=dum.children[idx]
            ret+=dum.n
        return ret
    

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
    T=tire()
    arr=[]
    x=0
    for i in range(n):
        s=input()
        T.insert(s)
        arr.append(s)
        x+=len(s)
    ans=0
    base=0
    for s in arr:
        ans+=T.search(s[::-1])*2
        base+=n*len(s)+x
    print(base-ans)

    pass
if __name__=='__main__':
    solve()