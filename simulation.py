import qutip
import numpy as np
from matplotlib import pyplot as plt

e = qutip.basis(2, 0)
g = qutip.basis(2, 1)

ee = e * e.dag()
gg = g * g.dag()

gamma = 0.5

L = np.sqrt(gamma) * g * e.dag()

H = qutip.qzero(2)

initial_state = e * e.dag()
times = np.linspace(0.0, 10.0, 100)

result = qutip.mesolve(H, initial_state, times, L, [ee, gg])

fig, ax = plt.subplots()
ax.plot(times, result.expect[0])
ax.plot(times, result.expect[1])
plt.show(fig)