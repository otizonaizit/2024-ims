import numpy as np


def f(x, r):
    """ Compute the logistic map for a given value of x and r. """
    return r * x * (1 - x)

def iterate_f(it, x, r):
    results = [x]
    for _ in range(it):
        x = f(x, r)
        results.append(x)
    return results