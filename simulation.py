import qutip
import numpy as np
from matplotlib import pyplot as plt

e = qutip.basis(2, 0)
g = qutip.basis(2, 1)

ee = e * e.dag()
gg = g * g.dag()

gamma = 0.5
L = np.sqrt(gamma) * g * e.dag()

def Hfunc(t, args):
    H0 = args[0]
    #w = 9 * np.exp(-(t/5.)**2)
    print(H0)
    H0 = 4 * H0
    print(H0)
    return H0

initial_state = e * e.dag()
times = np.linspace(0.0, 100, 100)

result = qutip.mesolve(Hfunc, initial_state, times, L, [ee, gg], args=[qutip.qeye(2)])

fig, ax = plt.subplots()
ax.plot(times, result.expect[0])
ax.plot(times, result.expect[1])
plt.show(fig)
