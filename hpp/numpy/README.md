# Anatomy of a numpy array
## one dimension, float64
![1d array](ndarray-memory-layout-1d.svg)

## two dimensions, square, float64
![2d array - square](ndarray-memory-layout-2d-square.svg)

## two dimensions, rectangular, int32
![2d array - rectangular](ndarray-memory-layout-2d-rectangular.svg)

## what about Python lists?
![memory layout of a Python list](python-list-memory-layout.svg)

## interesting attributes of numpy arrays
  - `x.data`, `x.data.hex()`, `x.data.format`, `x.tobytes()`
  - `x.flags`:
    - `OWNDATA`
    - `C_CONTIGUOUS`
    - `F_CONTIGUOUS`
    - more [flags](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html)

