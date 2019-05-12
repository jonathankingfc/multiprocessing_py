import time
import multiprocessing
import numpy as np


def calculatePrimes(upperBound):

    start = time.time()
    primes = []
    for n in range(2, upperBound + 1):
        if isPrime(n):
            primes.append(n)

    end = time.time()

    return(len(primes), end-start)


def isPrime(n):

    isPrime = True
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            isPrime = False
            break
    return isPrime


print(calculatePrimes(1000000))
