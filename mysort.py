import time
from multiprocessing import Pool
import numpy as np


def main(num_process):
    arrays = [np.random.rand(100) for i in range(0, 100000)]

    start = time.time()
    p = Pool(processes=num_process)
    p.map(my_sort, arrays)
    p.close()
    p.join()
    end = time.time()

    duration = end - start
    return duration


def my_sort(arr):
    np.sort(arr, kind="mergesort")
