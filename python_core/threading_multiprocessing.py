'''
Process: An instance of a program (e.g. Python interpreter)

+ Takes advantage of multiple CPU and cores
+ Separate memory space -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is started independently from other processes
+ Processes are interruptable/killable
+ One GIL for each process -> avoids GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread
- More memory usage
- IPC (inter-processing communication) is more complicated

Thread: An entity within a process that can be scheduled (also known as
"lightweight process"). A process can spawn multiple threads.

+ All threads within a process share the same memory
+ Lightweight
+ Starting a thread is faster than starting a process
+ Great for I/O-bound tasks

- Theading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks
- Non interruptable/killable
- Careful with race conditions

GIL: Global Interpreter Lock
- A lock that allows only one thread at a time to execute in Python
- Needed in CPython because memory management is not thread-safe
- Avoid:
    - Use multiprocessing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - Use Python as a wrapper for third-party libraries (C/C++) -> NumPy, SciPy
'''
from multiprocessing import Process, Value, Array, Pool
from multiprocessing import Lock as MLock, Queue as MQueue
from threading import Thread, Lock, current_thread
from queue import Queue
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        # time.sleep(0.1)


def processes_main():
    processes = []
    num_processes = os.cpu_count()

    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        print("Init process", p)
        processes.append(p)

    # start
    for p in processes:
        print("Start process", p)
        p.start()

    # join
    for i in processes:
        print("End process", p)
        p.join()

    print("End processes main")


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_100_to_array(number, lock):
    for i in range(100):
        time.sleep(0.01)
        for num in range(len(number)):
            with lock:
                number[num] += 1


def processes_using_lock():
    def threads_init_start_join(func, args):
        p1 = Process(target=func, args=args)
        p2 = Process(target=func, args=args)
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    lock = MLock()
    shared_number = Value('i', 0)
    print("Number at the beginning is", shared_number.value)
    threads_init_start_join(add_100, (shared_number, lock))
    print("Number at the end is", shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Array at the beginning is", shared_array[:])
    threads_init_start_join(add_100_to_array, (shared_array, lock))
    print("Array at the end is", shared_array[:])


def square(numbers, q):
    for i in numbers:
        q.put(i * i)
        time.sleep(0.01)


def make_negative(numbers, q):
    for i in numbers:
        q.put(-i)
        time.sleep(0.01)


def processes_using_queues():
    q = MQueue()
    numbers = range(1, 6)
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())


def cube(number):
    return number * number * number


def processes_using_pool():
    # map, apply, join, close
    pool = Pool()
    numbers = range(10)
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()
    print(result)


def threads_main():
    threads = []
    num_threads = 10

    # create processes
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        print("Init thread", t)
        threads.append(t)

    # start
    for t in threads:
        print("Start thread", t)
        t.start()

    # join
    for t in threads:
        print("End thread", t)
        t.join()

    print("End threads main")


global_variable = 0


def threads_using_lock():
    def increase():
        global global_variable
        local_copy = global_variable
        local_copy += 1
        time.sleep(0.1)
        global_variable = local_copy
        print(global_variable)

    def increase_no_lock(*args):
        ''' increase without lock -> racing conditions '''
        increase()

    def increase_lock_1(lock: Lock):
        ''' with lock.aquire() and lock.release() '''
        lock.acquire()
        increase()
        lock.release()

    def increase_lock_2(lock: Lock):
        with lock:
            increase()

    def run_thread_example(func):
        lock = Lock()
        print("Beginning example:", global_variable)
        tread1 = Thread(target=func, args=(lock,))
        tread2 = Thread(target=func, args=(lock,))
        tread1.start()
        tread2.start()
        tread1.join()
        tread2.join()
        print("End example:", global_variable, '\n')

    global global_variable
    global_variable = 0
    run_thread_example(increase_no_lock)
    global_variable = 0
    run_thread_example(increase_lock_1)
    global_variable = 0
    run_thread_example(increase_lock_2)


def threads_using_queues():
    q = Queue()
    for i in range(10):
        q.put(i)

    def process_queue(q, lock):
        item = q.get()
        with lock:
            print(f"{current_thread().name}, processing item={item}")
        time.sleep(1)
        q.task_done()

    def process_queue_at_once(q, lock):
        while not q.empty():
            process_queue(q, lock)

    def process_queue_infinite(q, lock):
        while True:
            process_queue(q, lock)

    lock = Lock()  # to sync using queue value in print

    def init_thread(func, i, daemon=False):
        print("== Init thread", i)
        t = Thread(target=func, args=(q, lock))
        ''' Daemon is the background thread that will die when main thread. If
        we don use it, then we need to pass signal to break infinite loop in
        process_queue_infinite(q, lock) function
        '''
        t.daemon = daemon
        print("== Start thread", i)
        t.start()

    for i in range(1, 4):
        init_thread(process_queue_at_once, i)
    for i in range(4, 7):
        init_thread(process_queue_infinite, i, True)

    print("== Pause 4sec to stop threads with process_queue_at_once()")
    time.sleep(4)  # just to wait for  threads to finish
    print("== Adding 10 more items")
    for i in range(10, 20):
        q.put(i)
    print("== Pause 2sec before q.join() to show it doesn't affect threads")
    time.sleep(2)
    print("== q.join to pause main thread until finish processing queue")
    q.join()
    print("== Finish")


if __name__ == '__main__':
#    print("Processes =====================")
#    processes_main()
#    print("Processes Locks =====================")
#    processes_using_lock()
#    print("Processes Queue =====================")
#    processes_using_queues()
    print("Processes Pool =====================")
    processes_using_pool()
#    print("Threads =====================")
#    threads_main()
#    print("Threads Locks =====================")
#    threads_using_lock()
#    print("Threads Queues =====================")
#    threads_using_queues()
