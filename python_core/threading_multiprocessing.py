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
from multiprocessing import Process
from threading import Thread
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


if __name__ == '__main__':
    # freeze_support()
    processes_main()
    threads_main()
