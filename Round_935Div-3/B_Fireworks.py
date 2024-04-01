from math import floor
for _ in range(int(input())):
    a,b,m=map(int, input().split())
    print(floor(m/a)+ floor(m/b)+2)