

input_1 = "input_5.txt"
output = "output5.txt"

with open(input_1, "r") as f:
    k = f.read().split()


item = iter(k)

T = int(next(item))

output_lines = []

for case in range(1, T+1):
    N = int(next(item))
    A = []
    for i in range(N):
        A.append(int(next(item)))

    N = len(A)
    total_length_sum = N * (N+1)*(N+2)//6

    frq = {}
    px = 0
    frq[px] = 1
    for x in A:
        px ^= x
        frq[px] = frq.get(px, 0) + 1

    sub_pairs = 0

    sub_triplets = 0

    for c in frq.values():
        if c>= 2:
            
            g = c*(c-1)//2
        else:
            g = 0
        sub_pairs += g
        if c>= 3:
            
            k = c*(c-1) * (c-2)//6
        else:
            k = 0
        
        sub_triplets +=k
    
    b = total_length_sum - sub_pairs - sub_triplets
    output_lines.append(f"Case #{case}: {b}")


with open(output, "w") as f:
    f.write(("\n").join(output_lines))