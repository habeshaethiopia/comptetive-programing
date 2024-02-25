s = [i for i in input()]
a = [0]
# print(a, b,sep='\n')
n=0
for i in range(len(s)-1):
    if i+1 <len(s) and s[i] == s[i+1]:
        n+=1
    a.append(n)

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(a[r-1]-a[l-1])