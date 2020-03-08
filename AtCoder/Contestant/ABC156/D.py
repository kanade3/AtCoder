import numpy as np


def prepare(n_p, MOD):
    nrt = int(n_p ** 0.5) + 1
    nsq = nrt * nrt
    facts = np.arange(nsq, dtype=np.int64).reshape(nrt, nrt)
    facts[0, 0] = 1
    for i in range(1, nrt):
        facts[:, i] = facts[:, i] * facts[:, i - 1] % MOD
    for i in range(1, nrt):
        facts[i] = facts[i] * facts[i - 1, -1] % MOD
    facts = facts.ravel().tolist()

    invs = np.arange(1, nsq + 1, dtype=np.int64).reshape(nrt, nrt)
    invs[-1, -1] = pow(facts[-1], MOD - 2, MOD)
    for i in range(nrt - 2, -1, -1):
        invs[:, i] = invs[:, i] * invs[:, i + 1] % MOD
    for i in range(nrt - 2, -1, -1):
        invs[i] = invs[i] * invs[i + 1, 0] % MOD
    invs = invs.ravel().tolist()

    return facts, invs


n, a, b = map(int, input().split())
n_f, n_b = prepare(n, 10 ** 9 + 7)
a_f, a_b = prepare(a, 10 ** 9 + 7)
b_f, b_b = prepare(b, 10 ** 9 + 7)

A=
print(2 ** n - 1 - A - B)
# print(2 ** n - 1 - (n_f[n] % (a_b[a] * a_b[n - a])) - (n_f[n] % (b_b[b] * b_b[n - b])))
# ans = 2 ** n - 1 - cmb(n, a) - cmb(n, b)
# print(ans % (10 ** 9 + 7))
