from sympy import factorint
from itertools import product

intput_1 = "input4.txt"
output = "output4.txt"

MOD = 1_000_000_007

def pre_inversefactor(K = 70):
    factor = [1] * (K + 1)
    for i in range (1, K+1):
        factor[i] = (factor[i-1]*i) % MOD
    inv = [1] * (K+1)
    inv[K] = pow(factor[K], MOD-2, MOD)
    for i in range(K, 0, -1):
        inv[i-1] = (inv[i]*i) % MOD
    return inv

def rising(N, k):
    if k == 0: return 1
    N %= MOD
    r = 1
    for t in range(k):
        r = (r * (N + t)) % MOD
    return r

def comb_largeN_smallk(N, k, invfact):
    return (rising(N, k) * invfact[k]) % MOD


def count_sequences(N, A, B, invfact):
    if B == 1:
        return 1 if A >= 1 else 0
    fac = factorint(B)                 # {prime: exponent}
    primes, exps = zip(*sorted(fac.items()))
    ans = 0
    for xvec in product(*[range(E+1) for E in exps]):
        # Build X from exponents xvec and check X <= A
        X = 1
        ok = True
        for p, x in zip(primes, xvec):
            if x:
                X *= pow(p, x)
                if X > A:
                    ok = False
                    break
        if not ok:
            continue

        ways = 1
        for E, x in zip(exps, xvec):
            ways = (ways * comb_largeN_smallk(N, x, invfact)) % MOD
            ways = (ways * comb_largeN_smallk(N, E - x, invfact)) % MOD
        ans = (ans + ways) % MOD
    return ans


with open(intput_1, "r") as f:
    k = f.read().split()

item = iter(k)

T = int(k[0])

invfact = pre_inversefactor(70)
outlines = []
idx = 1
for case in range(1, T+1):
    N = int(k[idx]); idx += 1
    A = int(k[idx]); idx += 1
    B = int(k[idx]); idx += 1

    a = count_sequences(N, A, B, invfact)

    outlines.append(f"Case #{case}: {a}")

with open(output, "w") as f:
    f.write(("\n").join(outlines))