import qutip
from emission import approach1
from emission import approach2
import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(linewidth=1e6, edgeitems=1e6)
'''
iterations = [1, 10, 20, 50, 75, 100]
results = []
for i in iterations:
    rho1 = approach1.simulate(20)
    rho2 = approach2.simulate(20, i)
    results.append(qutip.tracedist(rho1, rho2))

fig, ax = plt.subplots()
fig.suptitle('Comparison of approaches for system size 20')
ax.plot(iterations, results)
plt.xlabel("Number of trajectories")
plt.ylabel("Trace distance between approaches")
plt.show(fig)
'''
'''
rho1 = approach1.simulate(20)
rho2 = approach2.simulate(20, 100)
print(qutip.tracedist(rho1, rho2))
'''


fig, ax = plt.subplots()
fig.suptitle('Comparison of approaches for system size 20')
ax.plot([1, 5, 10, 20, 50, 100, 500], [0.30673003352847994, 0.1573762976663935, 0.08616482977122665, 0.0717424189475786, 0.04990978668050976, 0.01799839031121163, 0.00913792973457214])
plt.xlabel("Number of trajectories")
plt.ylabel("Trace distance between approaches")
plt.show(fig)
