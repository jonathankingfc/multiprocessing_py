import numpy as np
import os
import time
from multiprocessing import Pool


def main(num_processes):
    clean()
    start = time.time()
    p = Pool(processes=num_processes)
    result = p.map(fibonacci, list(range(1, 15)))
    p.close()
    p.join()
    end = time.time()
    fib_list = list(filter(None, result))  # fastest
    with open('fibonacci.txt', 'w') as f:
        for fib in fib_list:
            f.write("{}\n".format(fib))

    duration = end-start
    return duration


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def clean():
    if os.path.exists("fibonacci.txt"):
        os.remove("fibonacci.txt")
