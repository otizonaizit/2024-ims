#!/usr/bin/python3
# Run it with
# export CPU=0; /usr/bin/taskset --cpu-list $CPU ./bench.py $CPU
import os
import sys
import timeit

import numpy as np

CPU = sys.argv[1]
COUNT = (30, )
POWS = 2**np.arange(6, 23 + 1, dtype=int)

# Size of one dimensional numpy arrays of dtype 'float64':
# A fix overhead of 96 bytes plus a variable size:
# (n_items x 8 bytes)

def load_data_row(x, time_series):
    """Store one time series per raw"""
    for row, ts in enumerate(time_series):
        x[row,:] = ts
    return x

def load_data_column(x, time_series):
    """Store one time series per raw"""
    for column, ts in enumerate(time_series):
        x[:, column] = ts
    return x

for n_series in COUNT:
    float_items = POWS
    byte_sizes = n_series*float_items*8
    bads = []
    goods = []
    results = open(f'results_cpu{CPU}', 'wt')
    for i, len_one_series in enumerate(float_items):
        time_series = []
        for idx in range(n_series):
            time_series.append(np.zeros(len_one_series, dtype='float64'))
        x = np.zeros((n_series, len_one_series), dtype='float64')
        print('Timing good...')
        good = min(timeit.repeat(lambda: load_data_row(x, time_series), number=3))
        x = np.zeros((len_one_series, n_series), dtype='float64')
        print('Timing bad...')
        bad = min(timeit.repeat(lambda: load_data_column(x, time_series), number=3))
        print(f'{len_one_series}/{POWS[-1]} {good} {bad}')
        bads.append(bad)
        goods.append(good)
        results.write(f'{byte_sizes[i]} {good} {bad}\n')
        results.flush()
    results.close()

