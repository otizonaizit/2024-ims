# Computer Architecture

My Laptop:

  - Lenovo - T14 Gen 4
  - CPU i7-1365U: 
    - 2x "performance cores" (Intel Core) max 5.20 GHz (0.19 ns/cycle) with Hyper-Threading
    - 8x "efficient cores" (Intel Atom) max 3.90 GHz (0.26 ns/cycle)
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

