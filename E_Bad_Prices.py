t = int(input())
for i in range(t):
    n = int(input())
    prices = input()
    prices = prices.split()
    prices = list(map(int, prices))
    count= 0
    MIN = prices[-1]
    for i in range(n-2,-1,-1):
        if prices[i] > MIN:
            count += 1
        MIN = min(MIN, prices[i])
                                    
    print(count)
