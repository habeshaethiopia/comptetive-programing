for _ in range(int(input())):
    n=[int(i) for i in input()]
    for i in range(len(n)):
        m=i
        for j in range(i+1, len(n)):
            if n[i]>n[j] and n[j]%2!=n[i]%2:
                n[i],n[j]=n[j],n[i]
        
    print(n)

