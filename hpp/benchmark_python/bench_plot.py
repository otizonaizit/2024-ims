#!/usr/bin/python3
import os
import sys

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12

def get_xlabels(x):
    xlabels = []
    for value in x:
        b = int(2**value)
        if b < 1024:
            xlabels.append(f'{b}B')
        elif b < 1048576:
            xlabels.append(f'{b//1024}K')
        elif b < 1073741824:
            xlabels.append(f'{b//1024//1024}M')
        else:
            xlabels.append(f'{b//1024//1024//1024}G')
    return xlabels

def get_ylabels(y):
    ylabels = []
    for power in y:
        if power < -6:
            value = 10**(power+9)
            ylabels.append(f'{value}ns')
        elif power < -3:
            value = 10**(power+6)
            ylabels.append(f'{value}μs')
        elif power < 0:
            value = 10**(power+3)
            ylabels.append(f'{value}ms')
        else:
            value = 10**power
            ylabels.append(f'{value}s')
    return ylabels

prefix = 'results_'
for results in (f for f in os.listdir('.') if f.startswith(prefix)):
    cpu = results.removeprefix(prefix)

    title = f'Loading data ({cpu})'
    sizes, bads, goods = [], [], []
    with open(results, 'r') as fh:
        for line in fh:
            size, good, bad = line.split()
            bads.append(float(bad))
            goods.append(float(good))
            sizes.append(int(size))
    goods = np.array(goods)
    bads = np.array(bads)
    x = np.log2(sizes)
    y1 = np.log10(goods)
    y2 = np.log10(bads)
    # generate two plots: good+bad timings and slowdown plot
    plt.figure(figsize=(8.5, 7.5))
    p1, = plt.plot(x, y1, 'o')
    p2, = plt.plot(x, y2, 'o')
    plt.xlabel('size')
    plt.ylabel('load time (ms)')
    plt.xticks(x, get_xlabels(x), rotation=60)
    yticks = np.arange(min(np.floor(y1[0]),np.floor(y2[0])),
                       max(np.ceil(y1[-1]), np.ceil(y2[-1]))+1)
    plt.yticks(yticks, get_ylabels(yticks.astype(int)))
    plt.legend((p1, p2), ('contiguous', 'flipped'))
    miny = min(goods.min(), bads.min())
    maxy = max(goods.max(), bads.max())
    plt.title(title + ' - timings')
    plt.savefig(f'loading-timings-{cpu}.svg')

    # slowdown plot
    plt.figure(figsize=(8.5, 7.5))
    p1, = plt.plot(x, bads/goods, 'o')
    plt.xlabel('size')
    plt.ylabel('slowdown')
    plt.xticks(x, get_xlabels(x), rotation=60)
    plt.title(title + ' - slowdown')
    plt.savefig(f'loading-slowdown-{cpu}.svg')
