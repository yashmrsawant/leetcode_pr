
import numpy as np
from matplotlib import pyplot as plt
from time import time


Ns = np.arange(500, 3000, 100)

Ts = np.zeros((Ns.shape[0]))
c = 0
for N in Ns:

    A = np.random.randn(N, N)
    st = time()
    A_f = A.reshape((N*N))
    ed = time()
    Ts[c] = ed - st
    c = c + 1
    print("N = %d done..."%(N))

plt.plot(Ns, Ts)
plt.show()





