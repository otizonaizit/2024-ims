import os
import sys
import timeit

import matplotlib.pyplot as plt
import numpy as np
import threadpoolctl as th

TIMES_TO_REPEAT = 5

def main():
	times_to_plot = {}
	for arr_pow in range(6, 13):
		times_to_plot[2 ** arr_pow] = []
		for num_processes in range(1, 10):
			print(f"size: {2 ** arr_pow} (square matrix), over {num_processes} processes:")
			time_elapsed = min(timeit.repeat(
				lambda: test_run(arr_pow, num_processes), 
				repeat=5, number=TIMES_TO_REPEAT)) / 5
			print(time_elapsed)
			times_to_plot[2 ** arr_pow].append(time_elapsed)
	
	for power_of_2, elt in times_to_plot.items():
		plt.plot(list(range(1, 10)), elt, 'o', label=f"n={power_of_2}")
	plt.xlabel("limit num")
	plt.ylabel("seconds")
	plt.legend()
	plt.show()

def test_run(arr_size, num_processes):
	arr = np.zeros((2 ** arr_size, 2 ** arr_size), dtype="float64")
	with th.threadpool_limits(limits=num_processes, user_api='blas'):
		multiplied = arr @ arr

if __name__ == "__main__":
	main()
