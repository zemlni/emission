import qutip
from emission import approach1
from emission import approach2
import numpy as np

np.set_printoptions(linewidth=1e6, edgeitems=1e6)

rho1 = approach1.simulate(12)
rho2 = approach2.simulate(12)

print(qutip.tracedist(rho1, rho2))

print(rho1)
print(rho2)

print(rho1.tr())
print(rho2.tr())
