n = int(input())
string = input()
if n % 2 == 0:
    part1 = [string[i] for i in range(n) if  i % 2 == 0][::-1]
    part2 = [string[i] for i in range(n) if i % 2]
    print(''.join(part1 + part2))
else:
    part1 = [string[i] for i in range(n) if i % 2][::-1]
    part2 = [string[i] for i in range(n) if i % 2 == 0]
    print(''.join(part1 + part2)) 