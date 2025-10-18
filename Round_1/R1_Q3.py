input = "input3.txt"
output = "output3.txt"

with open(input, "r") as f:
    k = f.read().split()
idx = 1
item = iter(k)
T = int(k[0])

output_lines = []

for case in range(1, T+1):

    N = int(k[idx]); idx += 1
    A = int(k[idx]); idx += 1
    B = int(k[idx]); idx += 1

    seq = [1] * (2 * N -1) + [B]
    o = map(str, seq)

    output_lines.append(f"Case #{case}:" + " ".join(o))


with open(output, "w") as f:
    f.write("\n".join(output_lines))