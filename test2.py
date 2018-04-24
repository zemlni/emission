import qutip
import numpy as np

n = 12
gamma = 0.5
# L = np.sqrt(gamma) * g * e.dag()
L = np.sqrt(gamma) * qutip.destroy(n)

for level in range(n):
    probability = qutip.basis(n, n - level - 1).dag() * L.dag() * L * qutip.basis(n, n - level - 1)
    print("---------------------------")
    print(qutip.basis(n, n - level - 1))
    print(L * qutip.basis(n, n - level - 1))
    print(qutip.basis(n, n - level - 1).dag() * L.dag())
    print(probability)
    #print(level, probability)

