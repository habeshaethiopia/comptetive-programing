r = input()
n = len(r)
s= input()
stack = []
i =0 
must_get = s[i]
maxi = 0
count =  0
for j in range(n):
    
    if r[j] == s[i]:
        maxi = max(maxi , count)
        count = 0
        stack = []
        if i < len(s):
            i+=1 
    else:
        stack.append(r[j])
        count+=1
print(maxi)



