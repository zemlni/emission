# imports
import time
import qutip
import numpy as np
from matplotlib import pyplot as plt

def H_coeff(t, args):
    return 9*np.exp(-(t/5.)**2)

def simulate():
    for n in range(100, 101):
        e = qutip.basis(n, n-1) # alternate

        # expected values
        ev = [qutip.basis(n, k)*qutip.basis(n, k).dag() for k in range(n)]

        gamma = 0.1 # alternate

        L = np.sqrt(gamma)*qutip.destroy(n)

        ustate = qutip.basis(n, 0)
        sigma_ue = qutip.tensor(qutip.qeye(n), ustate*e.dag())
        H1 = (sigma_ue.dag() + sigma_ue)
        H = [[H1, H_coeff]]
        # H = qutip.qzero(n)

        rho = [[1/n for i in range(n)] for i in range(n)] # alternate
        initial_state = qutip.Qobj(rho, dims=[[n], [n]], shape=(n, n), isherm=True, type="oper")

        times = np.linspace(0.0, 1000.0, 100)

        result = qutip.mesolve(H, initial_state, times, L, ev)
        
        fig, ax = plt.subplots()
        for k in range(n):
            ax.plot(times, result.expect[k])
        plt.show(fig)
        

def main():
    start_time = time.time()
    simulate()
    print('runtime: ' + str(time.time()-start_time) + ' seconds')

if __name__ == '__main__':
    main()

#[[1/n for i in range(n)] for i in range(n)]