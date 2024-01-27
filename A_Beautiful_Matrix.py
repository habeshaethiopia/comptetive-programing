column =list(map(int, input().split()))
matrix = [column]
for i in range(len(column)-1):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in matrix:
    if 1 in i:
        x = matrix.index(i)
        y = i.index(1)
        break
print(abs(x-2)+abs(y-2))
