pos = input()
p1 = ["a8", "a1", "h1", "h8"]

if pos in p1:
    print(3)
elif pos[0] in ["a", "h"] or pos[1] in ["1","8"]:
    print(5)
else:
    print(8)


    