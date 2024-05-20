
import sys, threading
from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def main():
    print('hi')
    pass

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
# Fibonacci Sequence
memo ={}
def fib(i):
    if i is 0 or 1:
        return i
    
    memo[i] = fib(i - 1) + fib(i - 2)
    return memo[i]