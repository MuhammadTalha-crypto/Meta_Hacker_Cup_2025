

input_file = "input_2_off.txt"
output_file = "output.txt"

with open(input_file, "r") as f:
    d = f.read().split()

item = iter(d)

T = int(next(item))

out_lines = []

for test_case in range(1, T+1):
    N = int(next(item))
    A = []
    for i in range(N):
        A.append(int(next(item)))

    n = len(A)
    if n ==1:
        A[0]
    mx = max(A)
    md = 0
    for i in range(n-1):
        dist = A[i] - A[i + 1]
        if dist <0:
            dist = -dist
        if dist > md:
            md = dist
    if mx > md:
        hi = mx
    else:
        md
    
    def check_pros(a):
        i = 0
        while i < n:
            segment_min = A[i]
            j = i

            while j+1 < n:
                different = A[j] - A[j+1]
                if different < 0:
                    different = -different
                if different > a:
                    break
                j+= 1
                v = A[j]
                if v < segment_min:
                    segment_min = v
            if segment_min > a:
                return False
            i = j + 1
        return True


    lo = 0
    while lo < hi:
        mid = (lo + hi )//2
        if check_pros(mid):
            hi = mid
        else:
            lo = mid + 1
    out_lines.append(f"Case #{test_case}: {lo}")

with open("output.txt", "w") as f:
    f.write("\n".join(out_lines))

