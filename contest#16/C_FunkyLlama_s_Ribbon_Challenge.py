import sys, threading

input = lambda: sys.stdin.readline().strip()
def invr():
    return(map(int,input().split()))
def main():
    n,a,b,c=invr()
    path=[]
    
    ans=[]
    memo={}
    
       
            
    def dp(n):
        if n in memo:
            return memo[n]
        if n==0:
            return 0
        if n<0:
            return -1
        ans=-1
        for i in [a,b,c]:
            ans=max(dp(n-i)+1 or -1 ,ans)
        memo[n]=ans
        return ans
    
    print(dp(n))
     
    # print(memo)
    # print(max(ans))
        
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()