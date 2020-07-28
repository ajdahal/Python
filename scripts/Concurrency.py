# Concurrency, parallelism, python's concurrency methods comparism (threading,asyncio, multiprocessing), when to use concurrency and which module to use

# Concurrency: simultaneous occurrence (thread, task, process )
# cpu switches to different one by saving state, so that that can be restarted where it was interrupted

# threading, asyncio --> run on single processor, run one at a time --> find ways to speed up the overall process
# threading: OS knows about each thread and can interrupt thread at any time to start running a different thread --> pre-emptive multitaksing
# Asyncio: cooperative multitasking: tasks must cooperate by announcing when they are ready to be switched out (sight change in code makes this happen) 

# Parallelism:
# multiprocessing --> runs on multiple processor, python creates new processes(completely different program --> each process runs in its own python interpreter)

# Use of concurrency for different types of problems:
    # CPU-bound problems: program slow down due because CPU limits your program ( program gets CPU time after certain time gap )
    # I/O-bound problems: programs slow down due to I/O wait from some external resource - file system, network connections
'''
import requests
import time 


def download_site(url,session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            download_site(url,session)


if __name__ == "__main__":
    urls = ["https://realpython.com/python-concurrency", "https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32"]* 5
    start_time = time.time()
    download_all_sites(urls)
    print(f"Downloaded {len(urls)} in {time.time() - start_time} seconds")
    
'''
'''
import concurrent.futures
import threading

threading_local = threading.local()  # creates object that looks like global but is specific to each individual thread 

def get_session():
    if not hasattr(threading_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(urls):
    session = get_session()
    with session.get(urls) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site,urls)

if __name__ == "__main__":
    urls = ["https://realpython.com/python-concurrency", "https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32"]* 5
    start_time = time.time()
    download_all_sites(urls)
    print(f"Downloaded {len(urls)} in {time.time() - start_time} seconds")
'''
'''Problem with threading: we should really know what data is shared between threads,
threads interact in ways that are subtle and hard to detect, interactions can cause race conditions, intermittent bugs are difficult to find

Race Conditions happen because programmer has not sufficiently protected data accesses to prevent threads from interfering with each other, thread swapping can happen at any time (even in the middle of function)

requests.Session() is not thread-safe
'''
# asyncio Version
'''  single python object (called event loop) --> controls how and when each task gets run, event loop is aware about each task and it's state (ready, waiting), the event loop runs the task and then gets back the control only when the task is finished. It goes through each task and gives control to them necessarily 

async:  flag to python that tells function about to be defined uses await
await:  allows task to hand control back to the event loop, code awaits function call 

Any function that calls await needs to be marked with async
'''
'''
import asyncio
import time
import aiohttp

async def download_site(url,session):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(len(response.content),url))

async def download_all_sites(urls): # session is shared among the tasks
    async with aiohttp.ClientSession() as session: # session created as context manager 
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_site(session,url)) # creating list of tasks
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True) # keeps session context alive until all of the tasks have completed 

# asyncio scales far better than threading, each task takes far fewer resources and less time to create than a thread 

if __name__ == "__main__":
    urls = ["https://realpython.com/python-concurrency", "https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32"]* 5
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(urls)) # starting the event loop and telling it to run tasks 
    print(f"Downloaded {len(urls)} in {time.time() - start_time} seconds")
'''
''' problems : need special async version of libraries (notice, aiohttp used instead of sessions), if there is bug in code such that a task runs indefinately the control doesn't return back to event loop '''

# Multiprocessing Version:
'''

import multiprocessing

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site_m(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"Read {len(response.content)} from {url}")

def download_all_sites_m(urls):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site_m,urls)

if __name__ == "__main__":
    urls = ["https://realpython.com/python-concurrency", "https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32"]* 5
    start_time = time.time()
    download_all_sites_m(urls)
    print(f"Downloaded {len(urls)} in {time.time() - start_time} seconds") 
'''

''' Global Interpreter Lock/GIL 
multiprocessing --> standard library --> break the barrier of GIL and run code in multiple CPUs --> creaing new instance of python interpreter to run on each cpu --> heavyweight operation compared to threads but makes huge difference for correct problem
'''

''' problems with Multiprocessing Version:
Require Extra Setup
Spend time thinking about which variables will be accessed in each process
many solutions require more communication between the processes, this can add complexity to solution that a non-concurrent program would not need to deal with
'''

# How to speed up a CPU-Bound Program
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

# this code is running on a single core, using threadin or asyncio will slow it down further as the extra time is required on setting up threads or task and work is performed on only one cpu core

# Multiprocessing Version -- benificial here

import multiprocessing

def cpu_bound_m(number):
    return sum(i*i for i in range(number))

def find_sums_m(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound,numbers)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    
    start_time = time.time()
    find_sums_m(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

# When to use Concurrency:
''' 1. Do we need concurrency ?
    2. Which concurrency module do we need to use ? -- complexity and bugs difficult to find "premature optimization is the root of all evil in programming"
    3. Find out if the program is I/O (use asyncio when you can -- when we have libraries ported for asyncio, if no libraries use threading, threading when you must) bound or CPU bound (only gain from multiprocessing)'''

''' GIL / Global Interpreter Locks --> a lock that allows only one thread to hold the control of python interpreter, means only one thread can be in the state of execution at any point in time --> performance bottle neck for CPU-bound and multi-threaded code 

Python Memory Management: Reference counting, objects created in python have reference count variable that keeps track of number of reference that point to the object, when count reaches zero, memory occupied by object is released

Java Memory Management: Garbage Collection

sys.getrefcount()

reference variable needed protection from race conditions (two threads increase or decrease value simultaneously --> leaked memory that is never releases or incorrectly release memory while the reference to that object still exist --> crashes or weird bugs)

Reference count variable can be kept safe --> adding locks to all data structures shared across threads (multiple locks will exists resulting in deadlocks, slow performance due to repeaded acquisition and release of locks)

The program below takes almost same time to finish without threads and with threads
why? -- GIL prevented the CPU-bound threads from executing in parallel, process doesn't acquires the lock at once 
On I/O bound multi-threaded programs, lock is shared between threads while they are waiting for I/O

Thread releases GIL for sometime after continuous use, if another thread doesn't acquire GIL then the previous thread continues use of GIL.

We can check how long (how many instructions) the GIL is acquired by a process.

mport sys
sys.getcheckinterval()
'''

import time
from threading import Thread

COUNT = 500000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
middle1 = time.time()
print(middle1 - start)
t2.start()
middle2 = time.time()
print(middle2 - start)
t1.join()
middle3 = time.time()
print(middle3 - start)
t2.join()
middle4 = time.time()
print(middle4 - start)
end = time.time()
print('Time taken in seconds -', end - start)

''' Dealing with GIL

using multi-processing instead of multi-threading approach
using alternative python interpreters (Jpython, IronPython, PyPy -- donot have GIL) instead of CPython (has GIL)

'''