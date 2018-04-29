from emission import approach1
from emission import approach2
from matplotlib import pyplot as plt
import time
'''
t1 = []
t2 = []
for size in range(5, 200, 25):
    start_time = time.time()
    approach1.simulate(size)
    t1.append(time.time() - start_time)

    start_time = time.time()
    approach2.simulate(size, 1)
    t2.append(time.time() - start_time)
'''

fig, ax = plt.subplots()
fig.suptitle('Comparison of runtime')
ax.plot(range(5, 200, 25), [0.025160551071166992, 0.35996055603027344, 0.9071211814880371, 0.6418092250823975, 4.531381845474243, 6.838070631027222, 5.828044652938843, 9.73145604133606])
ax.plot(range(5, 200, 25), [0.741840124130249, 0.8468360900878906, 1.0418024063110352, 1.2523274421691895, 2.214359998703003, 1.9762024879455566, 2.267717123031616, 3.027034044265747])
plt.legend(["Density matrix", "Quantum trajectories"])
plt.xlabel("System size")
plt.ylabel("Runtime")
plt.show(fig)

print(t1)
print(t2)