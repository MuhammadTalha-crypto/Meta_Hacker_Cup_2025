input_1 = "input_6.txt"
output = "output6.txt"

with open(input_1, "r") as f:
    k = f.read().strip().split()

item = iter(k)
T = int(next(item))

output_lines = []

for case in range(1, T + 1):
    n = int(next(item))
    s = next(item)

    # Quick outcomes if only one type exists
    if 'A' not in s:
        j = "Bob"
    elif 'B' not in s:
        j = "Alice"
    else:
        L, R = 0, n - 1

        # find leftmost 'A' in [L..R]
        i = L
        while i <= R and s[i] != 'A':
            i += 1
        if i > R:
            j = "Bob"
        else:
            a = i
            # find rightmost 'B' in [L..R]
            jidx = R
            while jidx >= L and s[jidx] != 'B':
                jidx -= 1
            if jidx < L:
                j = "Alice"
            else:
                bpos = jidx
                # main loop: trim outer A/B pair each round
                while True:
                    if a > bpos:
                        j = "Alice"
                        break

                    # Alice eats at a, Bob eats at bpos
                    L, R = a + 1, bpos - 1
                    if L > R:
                        j = "Bob"
                        break

                    # next leftmost 'A' in [L..R]
                    i = L
                    while i <= R and s[i] != 'A':
                        i += 1
                    if i > R:
                        j = "Bob"
                        break
                    a = i

                    # next rightmost 'B' in [L..R]
                    jidx = R
                    while jidx >= L and s[jidx] != 'B':
                        jidx -= 1
                    if jidx < L:
                        j = "Alice"
                        break
                    bpos = jidx

    output_lines.append(f"Case #{case}: {j}")

with open(output, "w") as f:
    f.write("\n".join(output_lines) + "\n")
