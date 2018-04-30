from matplotlib import pyplot as plt
from emission import approach2
import numpy as np
from random import random

_, e1 = approach2.simulate(2, 100)

e2 = [1 - num for num in e1]

'''
emission_times = []
gamma = 0.5
time = 100
for _ in range(1000):
    emissions = 0
    for current_time in range(1, time):
        if random() < gamma ** 2 / 4 and emissions < 1:
            # emission
            emissions += 1
            emission_times.append(current_time)

expectations = [approach2.expect(i, emission_times) for i in range(100)]

e1 = expectations
e2 = [1 - num for num in expectations]
'''
fig, ax = plt.subplots()
ax.plot(np.linspace(0, 10, 100), e1)
ax.plot(np.linspace(0, 10, 100), e2)
fig.suptitle('Quantum Trajectories: Two Level System, 100 Trajectories')
plt.legend(["|e>", "|g>"])
plt.xlabel("Time")
plt.ylabel("Expectation value")
plt.show(fig)