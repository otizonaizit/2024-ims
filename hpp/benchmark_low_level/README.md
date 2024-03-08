# Low Level Memory Benchmark

These are the results of a low level memory benchmark (written in C) on my laptop.

  - Lenovo - T14 Gen 4
  - CPU i7-1365U: 
    - 2x "performance cores" max 5.20 GHz (0.19 ns/cycle) with Hyperthreading
    - 8x "efficient cores" max 3.90 GHz (0.26 ns per cycle) without HT
  - L1 (data) cache P-Core 48 KB
  - L1 (data) cache E-Core 32 KB
  - L2 cache P-Core 1280 KB
  - L2 cache E-Core 2048 KB (shared x4)
  - L3 cache 12 MB (shared P+E-Cores)
  - RAM DDR5-5200: 32GB (16GB soldered + 16GB bank):
    - Data rate 5200 MT/s, Transfer time 0.192 ns/cycle
    - Command rate (bus clock) 2600 MHz, Cycle time 0.385 ns
    - Interal clock 650 MHz, 1.54 ns
    - CAS Latency 34 cycles, Total latency = CAS latency x cycle = 13.09 ns, Throughput 41.6 GB/s
  - GPU Intel Iris, 1.30 GHz

![Graphical representation](topology.png)

Benchmarks run using the software [lmbench](http://lmbench.sourceforge.net/).

## Summary plots (details below)
![Memory Bandwidth P-core](bandwidth-cpu0.svg)
![Memory Bandwidth E-core](bandwidth-cpu10.svg)
![Memory Latency P-core](latency-cpu0.svg)
![Memory Latency E-core](latency-cpu10.svg)

## Benchmarks details:

  - Bandwidth (read), [bw_mem_rd](http://lmbench.sourceforge.net/man/bw_mem_rd.8.html). Allocate the specified amount of memory, zero it, and then time the reading of that memory as a series of integer loads and adds. Each 4-byte integer is loaded and added to accumulator. 

    [Results P-core](cpu0-bwr.csv) and [Results E-core](cpu10-bwr.csv) (block size in MB, bandwith in MB/s)
  - Bandwidth (write),[bw_mem](http://lmbench.sourceforge.net/man/bw_mem.8.html). Allocate twice the specified amount of memory, zero it, and then time the copying of the first half to the second half. 

    [Results P-core](cpu0-bww.csv) and [Results E-core](cpu10-bww.csv) (block size in MB, bandwith in MB/s)
  - Latency (sequential access), [lat_mem_rd](http://lmbench.sourceforge.net/man/lat_mem_rd.8.html). Run two nested loops. The outer loop is the stride size of 128 bytes. The inner loop is the block size. For each block size, create a ring of pointers that point backward one stride. Traverse the block by `p = (char **)*p` in a for loop and time the load ladency over block. 

    [Results P-core](cpu0-lseq.csv) and [Results E-core](cpu10-lseq.csv) (block size in MB, latency in ns)
  - Latency (random access). Like above, but with a stride size of 16 bytes. 

    [Results P-core](cpu0-lrnd.csv) and [Results E-core](cpu10-lrnd.csv) (block size in MB, latency in ns)



