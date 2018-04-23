import qutip
import numpy as np
from random import random
import time
from matplotlib import pyplot as plt

def simulate(n):
    final_states = []
    for i in range(1):
        e = qutip.basis(n, n-1)

        initial_state = e

        gamma = 0.5
        #L = np.sqrt(gamma) * g * e.dag()
        L = np.sqrt(gamma)*qutip.destroy(n)

        #H0 = qutip.sigmax()
        H0 = qutip.qzero(n)

        H = H0 + L * L.dag()

        emission_time = random() * 90

        times = np.linspace(0.0, emission_time, int(emission_time))

        options = qutip.Options()
        options.store_final_state = True
        options.nsteps = options.nsteps * 10
        #options.store_states = True
        result = qutip.mesolve(H, initial_state, times, [], [], options=options)

        state = result.states[-1]
        state = L * state
        state = state.unit()

        times = np.linspace(emission_time, 100, int(100 - emission_time))

        result = qutip.mesolve(H, state, times, [], [], options=options)

        final_states.append(result.states[-1])

    '''
    sum = qutip.qzero(n)
    for current in final_states:
        sum = np.add(sum, current * current.dag())
    '''

runtimes = []
#for n in range(5, 500, 10):
n = 500
print(n)
start_time = time.time()
result = simulate(n)
runtimes.append(time.time() - start_time)

'''
fig, ax = plt.subplots()
ax.plot(range(5, 1000, 10), runtimes)
plt.show(fig)
'''
