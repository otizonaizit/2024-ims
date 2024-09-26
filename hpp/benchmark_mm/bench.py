
import os
import sys
import timeit

import numpy as np
import threadpoolctl as th


def multiply_matrix(N, T):
    x = np.zeros((N, N), dtype="float64")
    with th.threadpool_limits(limits=T, user_api='blas'):
        y = x @ x


if __name__ == '__main__':
    processes = sys.argv[1]
    times = []
    results = open(f'results_{processes}', 'wt')
    for n_threads in range(len(os.sched_getaffinity(0))):
        for matrix_size in [30, 300, 3000]:
            time = min(timeit.repeat(lambda: multiply_matrix(N=matrix_size, T=n_threads), number=5))/5
            results.write(f'{n_threads}_{matrix_size}_{time}\n')
            results.flush()
    results.close()
    
            
  

