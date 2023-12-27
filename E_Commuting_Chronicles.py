"""
x=list(map(int, input().split()))
n=x[0]-1
m=x[1]-1
matrix=[]

for i in range(n):
    row=list(map(int, input().split()))
    matrix.append(row)
turn=0
i=0
j=0
found=False
while i<n:
    while j<m:
        if (matrix[i][j]=='S' or matrix[i][j]=='T' )and not found:
            found=True
        else:
            j+=1
        if found:
            if matrix[i][j]=='*':
                i+=1
                turn+=1
            elif matrix[i][j]=='.':
                j+=1
"""


rows, cols = map(int, input().split())

grid = []
for _ in range(rows):
    row = list(input())
    grid.append(row)


def solve(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "TS":
                # mark the left until we get '*', 'T' or 'S', or we reach the end
                i = c - 1
                while i >= 0 and grid[r][i] == ".":
                    grid[r][i] = "M"
                    i -= 1
                if (
                    i >= 0 and grid[r][i] in "TS"
                ):  # Case 1: check if we can reach with no turn
                    return True

                # mark the right until we get '*', 'T' or 'S', or we reach the end
                i = c + 1
                while i < cols and grid[r][i] == ".":
                    grid[r][i] = "M"
                    i += 1
                if (
                    i < cols and grid[r][i] in "TS"
                ):  # Case 1: check if we can reach with no turn
                    return True

    for c in range(cols):
        r = 0
        while r < rows:
            if grid[r][c] in "TSM":
                r += 1
                while r < rows and grid[r][c] == ".":
                    r += 1
                if r < rows and grid[r][c] in "TSM":
                    return True
            r += 1
    return False


# transpose the grid for the second case
transposed_grid = [[""] * rows for _ in range(cols)]
for r in range(rows):
    for c in range(cols):
        transposed_grid[c][r] = grid[r][c]

# Case 2: Vertical turn
is_found = solve(grid, rows, cols)
if is_found:
    print("YES")
    exit()

# Case 3: Horizontal turn
if solve(transposed_grid, cols, rows):
    print("YES")
else:
    print("NO")
    