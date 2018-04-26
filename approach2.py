import qutip
import numpy as np
from random import random
import time
from matplotlib import pyplot as plt
import math
np.set_printoptions(linewidth=1e6, edgeitems=1e6)

def simulate(n):
    final_states = []
    iterations = 100
    for i in range(iterations):
        e = qutip.basis(n, n - 1)

        state = e

        gamma = 0.5
        #L = np.sqrt(gamma) * g * e.dag()
        L = np.sqrt(gamma)*qutip.destroy(n)


        lamb = 0.05
        H0 = 1 / 2 + qutip.num(n)
        #H0 = 1/2 + qutip.num(n) + lamb * (qutip.position(n)) ** 4
        H = H0 - np.complex(1) * L * L.dag()

        options = qutip.Options()
        options.store_final_state = True
        options.nsteps = options.nsteps * 10000
        #options.method = "bdf"
        num_emissions = 0

        for level in range(n):
            if random() > gamma ** level:
                num_emissions = level
                break

        #num_emissions = int(math.floor(random() * n))
        emission_times = sorted([random() * 80 + 10 for _ in range(num_emissions)])
        time = 100
        prev_time = 0
        emissions = 0
        for current_time in range(1, time):
            if random() < gamma ** 2 and emissions < n - 1:
                #emission
                state = L * state
                state = state.unit()
                emissions += 1
            times = np.linspace(prev_time, current_time, 10)
            result = qutip.mesolve(H, state, times, [], [], options=options)
            state = result.states[-1]
            prev_time = current_time

        '''
        prev_time = 0
        for emission_time in emission_times:
            state = state.unit()
            times = np.linspace(prev_time, emission_time, 10)
            result = qutip.mesolve(H, state, times, [], [], options=options)

            state = result.states[-1]
            state = L * state

            prev_time = emission_time
        
        times = np.linspace(prev_time, 100, 5)
        result = qutip.mesolve(H, state, times, [], [], options=options)
        '''
        final_states.append(state)
        print("iteration: " + str(i))

    sum = qutip.qzero(n)
    for current in final_states:
        sum = np.add(sum, current * current.dag())
    sum /= iterations

    return sum

'''
runtimes = []
#for n in range(5, 500, 10):
n = 12
start_time = time.time()
result = simulate(n)
runtimes.append(time.time() - start_time)
'''

'''
fig, ax = plt.subplots()
ax.plot(range(5, 1000, 10), runtimes)
plt.show(fig)
'''
