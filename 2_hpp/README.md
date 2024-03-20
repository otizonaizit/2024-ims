# High-performance Python: a sweeping overview of computer architecture
**Important**: these are instructor notes, remove this file before showing the materials to the students. The notes can be added after the lecture, of course.

## Introduction

  - [Puzzle](puzzle.ipynb) (how swapping two nested for-loops makes out for a &gt;27× slowdown
  - Let students play around with the notebook and try to find the "bug"
  - A more thorough benchmark using the same code is [here](benchmark_python/)

## A digression in CPU architecture and the memory hierarchy

  - Go to [A Primer in CPU architecture](architecture)
  - The need for a hierarchical access to data for the CPU should be clear now ➔ the "starving" CPU problem
  - Have a look at the historical evolution of [speeds](speed/) of different components in a computer:
    - the CPU clock rate
    - the memory (RAM) bandwidth, latency clock rate
    - the storage media access rates

  - Measure size and timings for the memory hierarchy on my machine with a low level [C benchmark](benchmark_low_level)

## Back to the Python benchmark (second try)

  - can we explain what is happening?
  - it must have to do with the good (or bad) use of cache properties
  - but how are numpy arrays laid out in memory?

## Anatomy of a numpy array

  - [memory layout of numpy arrays](numpy)

## Back to the Python benchmark (third try)
  - can we explain what is happening now? Yes, more or less ;-)
  - quick fix for the [puzzle](puzzle.ipynb): try and add `order='F'` in the "bad" snippet and see that is "fixes" the bug ➔ why?

Notes on the [Python benchmark](benchmark_python/):
  - while running it attached to the P-core (`cpu0`), the P-core was running under a constant load of 100% (almost completely user-time) and at a fixed frequency of 3.8 GHz, where the theoretical max would be 5.2 GHz
  - while running it attached to the E-core (`cpu10`), the E-core was running under a constant load of 100% (almost completely user-time) and at a fixed requency of 2.5 GHz, where the theoretical max would be 3.9 GHz
  - ... ➔ the CPU does not "starve" because it scales its speed down to match the memory throughput? Or I am misinterpreting this? This problem which at first sight should be perfectly memory-bound, becomes CPU-bound, or actually, exactly balanced? ;-)

## Excerpts of parallel Python
  - [The dangers and joys of automatic parallelization](parallel) (like in numpy linear algebra routines) and the use of clusters/schedulers (but also on your laptop)

## Concluding remarks
  - how is all of this relevant for the users of a computing cluster?
