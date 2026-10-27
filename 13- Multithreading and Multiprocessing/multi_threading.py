### Multithreading
## When to use Multi Threading
### 1- I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
### 2- Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")


def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter: {letter}")


## create 2 threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

t = time.time()

# Start the thread
thread1.start()
thread2.start()

# Wait the threads to complete
thread1.join()
thread2.join()

finished_time = time.time() - t

print(finished_time)
