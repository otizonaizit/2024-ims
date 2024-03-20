import os
import sys
import numpy as np
import matplotlib
import itertools
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12

caches = ( {'cpu0' : 48*1024     , 'cpu10' : 32*1024},
           {'cpu0' : 1280*1024   , 'cpu10' : 2048*1024},
           {'cpu0' : 12*1024*1024, 'cpu10' : 12*1024*1024},
         )

def get_labels(x):
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


# manually set ticks, to disable, set ticks = None

line = np.linspace(1, 10, 9, endpoint=False)
yticks = list(line)+list(line*10)+list(line[:2]*100)

ylabels = (1, 10, 100)
ticks = {'l': {'cpu0' : (yticks, [str(int(i)) if i in ylabels else '' for i in yticks]),
               'cpu10': (yticks, [str(int(i)) if i in ylabels else '' for i in yticks])},
         'bw': {'cpu0' : (range(15,31), range(15,31)),
                'cpu10': (range(7,22), range(7,22))},
         }

# manually set limits, to disable set to ylim = None

ylim = {'l' : {'cpu0' : (1, 200),
               'cpu10': (1, 200)},
        }

# load all CSV files
for cpu in ('cpu0', 'cpu10'):
    for type_ in ('bw', 'l'):
        if type_ == 'bw':
            suffix = ('r', 'w')
            ylabel = ''
            title = f'Memory Bandwidth ({cpu}) [GB/s]'
            legend1, legend2 = 'read', 'write'
            pic = f'bandwidth-{cpu}.svg'
            plt_func = plt.plot
        else:
            suffix = ('seq', 'rnd')
            ylabel = ''
            title = f'Memory Latency ({cpu}) [ns]'
            legend1, legend2 = 'sequential access', 'random access'
            pic = f'latency-{cpu}.svg'
            plt_func = plt.semilogy


        data1 = np.loadtxt(f'{cpu}-{type_}{suffix[0]}.csv', delimiter=',')
        data2 = np.loadtxt(f'{cpu}-{type_}{suffix[1]}.csv', delimiter=',')

        # convert to bytes and then to the corresponding power of two

        if type_ == 'bw':
            x1 = np.log2(data1[:,0]*1024*1024).round()
            y1 = data1[:,1]/1024
            x2 = np.log2(data2[:,0]*1024*1024).round()
            y2 = data2[:,1]/1024
        else:
            x1 = np.log2(data1[::2,0]*1024*1024).round()
            y1 = data1[::2,1]
            x2 = np.log2(data2[::2,0]*1024*1024).round()
            y2 = data2[::2,1]
            ylabels = None


        xlabel = 'block size'
        xlabels = get_labels(x1)

        plt.figure(figsize=(8.5,7.5))
        p1, = plt_func(x1, y1, 'o')
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        p2, = plt_func(x2, y2, 'o')
        if ylim and type_ in ylim:
            plt.ylim(*ylim[type_][cpu])
        plt.xticks(x1, xlabels, rotation=60)
        if ticks and type_ in ticks:
            plt.yticks(*ticks[type_][cpu])
        plt.legend((p1, p2), (legend1, legend2))
        miny = min(y1.min(), y2.min())
        maxy = max(y1.max(), y2.max())
        # caches
        for idx, cache in enumerate(caches):
            level = idx + 1
            size = np.log2(cache[cpu])
            plt.plot((size, size), (miny, maxy),
                     color = 'darkblue', alpha=0.4)
            plt.text(size-1, (miny+maxy)/2, f'L{level}\n⟵',
                     color='darkblue', verticalalignment='top')

        plt.title(title)
        plt.savefig(pic)


