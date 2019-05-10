import threading
import time
import multiprocessing
import numpy as np


def my_sort(arr_size, num_arrays, sort_type):
    for i in range((int(num_arrays))):
        arr = np.random.rand(arr_size)
        np.sort(arr, kind=sort_type)


def mp_test(num_arrays, num_process, arr_size, sort_type):
    process_list = []
    start = time.time()
    for i in range(num_process):
        arrays_per_process = num_arrays/num_process
        p = multiprocessing.Process(target=my_sort, name='thread{}'.format(
            i), args=(arr_size, arrays_per_process, sort_type))
        process_list.append(p)
        p.start()
    for p in process_list:
        p.join()
    end = time.time()
    print("Processes: {}\t".format(num_process))
    print("Array Size: {}\t".format(arr_size))
    print("Sort Type: {}\t".format(sort_type))
    print("Time: {}\n".format(end-start))


def threading_test(num_arrays, num_threads, arr_size, sort_type):
    threads_list = []
    start = time.time()
    for i in range(num_threads):
        arrays_per_thread = num_arrays/num_threads
        t = threading.Thread(target=my_sort, name='thread{}'.format(
            i), args=(arr_size, arrays_per_thread, sort_type))
        threads_list.append(t)
        t.start()
    for t in threads_list:
        t.join()
    end = time.time()
    print("Threads: {}\t".format(num_threads))
    print("Array Size: {}\t".format(arr_size))
    print("Sort Type: {}\t".format(sort_type))
    print("Time: {}\n".format(end-start))


threading_test(100000, 1, 10000, "quicksort")
threading_test(100000, 5, 10000, "quicksort")
threading_test(100000, 10, 10000, "quicksort")
mp_test(100000, 1, 10000, "quicksort")
mp_test(100000, 5, 10000, "quicksort")
mp_test(100000, 10, 10000, "quicksort")
