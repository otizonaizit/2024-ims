# A Primer in CPU architecture
  - Primer on CPU (x86_64) architecture and the memory hierarchy:
    - CPU registers ≈ 160 (plus another ~500 model specific), latency: 0 cycles, capacity: 8 bytes
    - x86-64 instruction set, with ≈ 2000 instructions with mnemonic (plus an unknown number of "undocumented" instructions ~ 10k)
    - (single instruction, mutiple data [8 or 16 data units]) SIMD CPUs
    - L-Caches: L1/L2/L3, with cache lines of 128B, latencies: 1-40 cycles, capacity:  ~KB and ~MB
    - Main memory: RAM pages 4KB or 64KB, latency: 50~100 cycles, capacity ~GBs
    - Storage (local disks): disk transfer blocks 4KB to 64MB, latency: 0.1ms (300k cycles), capacity: ~TBs
    - Remote Storage (network): typically limited by ethernet connection (1-10 GB/s), latency: 10~100 ms, capacity: ∞
  - understand the trade-offs involved:
      - capacity
      - latency ≈ (time-when-data-available-on-output-pins – time-when-data-requested) ➔ measured in ns: clock_ticks × number-of-ticks-per-operation
      - bandwidth ≈ clock_tick × data-transfer/tick × bus-width 
      - volatility
      - cost
      - physical limits (heat dissipation, density, size, lifetime)
  - exploit temporal and spacial locality of data to overcome the "starving CPU" problem

# …and what about the GPU?
![GPU vs CPU architecture](GPUvsCPU-architecture.png)
  - a GPU has many (n the order of hundreds) SIMT (single instruction, multiple thread) cores, so called SMs (Streaming Multiprocessors), each one with local L1 and shared L2 caches, and shared RAM (due to to the high parallelism, with huge bandwidth, in the order of ~1TB/s
  - The SMs are specialized on data types. In order of abundance, the following data types are supported: int8, int32, int64, float16, float32, float64
  - performance depends on:
    - memory bandwidth: usually higher than CPU's RAM
    - "math" bandwidth: usually higher than CPU's, but much more limited in capability; for example branches (if/else) are expensive
    - latency: usually much higher than  CPU's ➔ the more parallel threads are run the less the price of high latency is paid (latency "hiding") 
    - spatial locality is extremely critical
  - A portion of the GPU-RAM is accessible to the CPU ➔ the GPU performs the copies
  - The PCI-Bus bottleneck: data needs to flow from main (CPU) memory to GPU memory and back!
  - Problems on a cluster: the GPU does not really support simultanous multiple users payloads!

# Computer Architecture ( a concrete example)
My Laptop:

  - Lenovo - T14 Gen 4
  - CPU i7-1365U: 
    - 2× "performance cores" (Intel Core) max 5.20 GHz (0.19 ns/cycle) with Hyper-Threading
    - 8× "efficient cores" (Intel Atom) max 3.90 GHz (0.26 ns/cycle)
  - L1 (data) cache P-Core 48 KB
  - L1 (data) cache E-Core 32 KB
  - L2 cache P-Core 1280 KB
  - L2 cache E-Core 2048 KB (shared x4)
  - L3 cache 12 MB (shared P+E-Cores)
  - RAM DDR5-5200: 32GB (16GB soldered + 16GB bank):
    - Data rate 5200 MT/s, Transfer time 0.192 ns/cycle
    - Command rate (bus clock) 2600 MHz, Cycle time 0.385 ns
    - Internal clock 650 MHz, 1.54 ns
    - CAS Latency 34 cycles, Total latency = CAS latency x cycle = 13.09 ns, Throughput 40.6 GB/s
  - DMI (Direct Media Interface): 8×16 GT/s (≈128 GB/s)
  - PCI Express bridges:
    - Graphics: 16 GT/s (≈ 8 GB/s)
    - 2× Thunderbolt: 2.5 GT/s (≈ 1 GB/s) and 16 GT/s (≈ 8 GB/s)
  - GPU Intel Iris, Internal clock 300 Mhz-1.30 GHz, memory 4 GB/2.1 GHz with a bandwidth of 68 GB/s

![Graphical representation](topology.png)

