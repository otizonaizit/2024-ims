import multiprocessing as mp
import time

import numpy as np
import threadpoolctl as th


def benchmark(p):
    N = [100, 500, 1000, 1500, 2000, 2500]
    C = [2, 4, 6, 8]

    times_per_config = dict()

    for n in N:
        for c in C:
            start = time.time()
            x = np.zeros((n, n), dtype="float64")
            with th.threadpool_limits(limits=c, user_api='blas'):
                y = x @ x
            end = time.time()
            times_per_config[(c, n, p)] = end - start
            print(c, n, p, end - start)


if __name__ == '__main__':
    C = [2, 4, 6, 8]
    processes = list()
    for c in C:
        processes.append(mp.Process(target=benchmark, args=(c,), daemon=False))
        processes[-1].start()
    for process in processes:
        process.join()


