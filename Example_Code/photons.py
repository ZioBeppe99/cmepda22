import random
import time

import matplotlib.pyplot as plt
import numpy as np

N = 1000000
THICKNESS = 0.200 #mm

lambda_ = 0.100 # mm

num_absorbed = 0.

def eff_simple(num_events):
    abs_z = []
    t0 = time.time()
    for i in range(num_events):
        z = random.expovariate(1. / lambda_)
        if z < THICKNESS:
            abs_z.append(z)
    elapsed_time = time.time() - t0
    print(f'Running time: {elapsed_time}')
    return abs_z

def eff_vectorized(num_events): #riduce il tempo di un fattore venti per un milione di fotoni
    t0 = time.time()
    abs_z = np.random.exponential(lambda_, size=num_events)
    abs_z = abs_z[abs_z <= THICKNESS] #mask (array slicing e indexing, si prende un sottoinsieme di un array)
    elapsed_time = time.time() - t0
    print(f'Running time: {elapsed_time}')
    return abs_z


z = eff_simple(N)
z = eff_vectorized(N)
quantum_efficiency = len(z) / N
print(f'Quantum efficiency: {quantum_efficiency} s')

#plt.hist(abs.z, bins=100)
#plt.yscale('log')
#plt.show()

#possiamo ridurre il tempo di esecuzione utilizzando il metodo di vettorizzazione

