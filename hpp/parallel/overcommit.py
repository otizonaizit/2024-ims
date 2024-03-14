import sys
import numpy as np

import matplotlib.pyplot as plt
import threadpoolctl as th
import timeit



# N = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
# x = np.zeros((N, N), dtype="float64")

time_dict = {}

Ns = [1000, 2000, 3000, 4000, 5000]
# Ns = [1, 2, 5, 100, 500]

for n in Ns:
    x = np.zeros((n, n), dtype="float64")
    time_dict[n] = []
    for limit_num in range(1,6):
        with th.threadpool_limits(limits=limit_num, user_api='blas'):
            time = timeit.timeit(lambda: x @ x, number=5)
            time_dict[n].append(time)
            print(f"N = {n}, threads = {limit_num}: {time} seconds")


for n in time_dict:
    plt.plot(list(range(1,6)), time_dict[n], 'o', label=f"n={n}")
plt.xlabel("limit num")
plt.ylabel("seconds")
plt.legend()
plt.savefig("plot.jpg", dpi=600)
plt.show()