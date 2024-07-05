# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.mem={}
    def fib(self, n: int) -> int:
        '''Top-Down approch'''
        # if n==1:
        #     self.mem[1]=1
        #     return 1
        # if n==0:
        #     self.mem[0]=0
        #     return 0
        # elif n not in self.mem:
        #     self.mem[n]=self.fib(n-1)+ self.fib(n-2)
        # return self.mem[n]
        '''Bottom-up'''
        a1=1
        a0=0
        for i in range(n):
            new=a1+a0
            a0=a1
            a1=new
        return a0