for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        r = input()
        matrix.append(r)
    c = matrix[0].count("1")
    for i in range(1, n):
        if c:
            if c == matrix[i].count("1") or c == 0:
                print("SQUARE")
                break
            else:
                print("TRIANGLE")
                break
        c = matrix[i].count("1")
    else:
        print("SQUARE")
