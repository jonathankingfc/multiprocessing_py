import time
from multiprocessing import Pool
import os


def main(num_process):
    start = time.time()
    p = Pool(processes=num_process)
    result = p.map(isPrime, list(range(2, 1000000)))
    p.close()
    p.join()
    end = time.time()
    prime_list = list(filter(None, result))  # fastest

    with open('primeNumbers.txt', 'w') as f:
        for prime in prime_list:
            f.write("{}\n".format(prime))

    duration = end-start
    return duration


def isPrime(n):

    isPrime = True
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            isPrime = False
            break
    if isPrime:
        return n
    else:
        return None


def clean():
    if os.path.exists("primeNumbers.txt"):
        os.remove("primeNumbers.txt")
