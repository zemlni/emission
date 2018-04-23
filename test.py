from qutip import *
import numpy as np
from matplotlib import pyplot as plt


ground = basis(2, 0)

excited = basis(2, 1)

sigma_ge = ground * excited.dag()  # |g><e|

c_ops = []  # Build collapse operators

gamma = 6  # Atomic decay rate

c_ops.append(np.sqrt(4*gamma/9) * sigma_ge) # 4/9 e->g

t = np.linspace(-15, 15, 100) # Define time vector

psi0 = excited # Define initial state

state_GG = ground# Define states onto which to project

sigma_GG = state_GG * state_GG.dag()

state_ee = excited

sigma_ee = state_ee * state_ee.dag()

g = 5  # coupling strength
H1 = sigmax()  # time-dependent term

def H1_coeff(t, args):
    return np.cos(t)

H = [[H1,H1_coeff]]

output = mesolve(H, psi0, t, c_ops, [sigma_ee, sigma_GG])

fig, ax = plt.subplots()
ax.plot(t, output.expect[0])
ax.plot(t, output.expect[1])
plt.show(fig)