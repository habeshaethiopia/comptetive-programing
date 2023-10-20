n_k = input()
n_k = n_k.split()
n = int(n_k[0])
k = int(n_k[1])

scores = input()
scores = scores.split()
scores = [int(i) for i in scores]
count = 0
for i in scores:
    if i >= scores[k - 1] and i > 0:
        count += 1
print(count)
