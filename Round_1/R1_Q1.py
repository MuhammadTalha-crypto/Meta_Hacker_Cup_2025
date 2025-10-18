

input_file = 'input.txt'
output_file = 'output.txt'


with open(input_file, "r") as f:
    inp1 = f.read().split()

a = iter(inp1)

b = int(next(a))

output_lines = []

for i in range(1, b + 1):
    N = int(next(a))
    h = []
    for k in range(N):
        h.append(int(next(a)))
    best = 0
    if len(h) > 1:
        j = 0
        for f in range(len(h) - 1):
            y = abs(h[f] - h[f+1])
            if y > j:
                j  = y
        best = j
    output_lines.append(f"Case #{i}: {best}")

with open(output_file, "w") as u:
    u.write("\n".join(output_lines))




