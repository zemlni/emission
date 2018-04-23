# imports
import time
import qutip
import numpy as np
from matplotlib import pyplot as plt

def simulate(n):

    e = qutip.basis(n, n-1) # alternate

    # expected values
    ev = [qutip.basis(n, k)*qutip.basis(n, k).dag() for k in range(n)]

    gamma = 0.1 # alternate

    L = np.sqrt(gamma)*qutip.destroy(n)

    H = 1/2 + qutip.num(n)
    #H = qutip.qzero(n)

    #rho = [[1/n for i in range(n)] for i in range(n)] # alternate
    rho = e * e.dag()
    #initial_state = qutip.Qobj(rho, dims=[[n], [n]], shape=(n, n), isherm=True, type="oper")
    initial_state = e

    times = np.linspace(0.0, 100.0, 100)

    return qutip.mesolve(H, initial_state, times, L, ev)


def main():
    start_time = time.time()
    n = 50
    result = simulate(n)
    print('runtime: ' + str(time.time()-start_time) + ' seconds')
    fig, ax = plt.subplots()
    times = np.linspace(0.0, 100.0, 100)
    for k in range(n):
        ax.plot(times, result.expect[k])
    plt.show(fig)

if __name__ == '__main__':
    main()

#[[1/n for i in range(n)] for i in range(n)]