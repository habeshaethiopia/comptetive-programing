def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def main():
    # Read input from file
    with open('macarie.in', 'r') as infile:
        # Read N and Q
        N, Q = map(int, infile.readline().strip().split())
        
        # Read array A
        A = list(map(int, infile.readline().strip().split()))
        
        # Read positions Poz
        Poz = list(map(int, infile.readline().strip().split()))
    
    # Generate all divisors
    all_divisors = []
    for number in A:
        all_divisors.extend(find_divisors(number))
    
    # Sort the list of divisors
    all_divisors.sort()
    
    # Prepare output based on Poz
    result = [all_divisors[pos - 1] for pos in Poz]
    
    # Write result to output file
    with open('macarie.out', 'w') as outfile:
        outfile.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":
    main()