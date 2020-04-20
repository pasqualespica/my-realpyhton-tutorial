# Speed Up Your Python Program With Concurrency
https://realpython.com/python-concurrency/

https://github.com/realpython/materials/tree/master/concurrency-overview


In this article, you’ll learn the following:

- What concurrency is
- What parallelism is
- How some of Python’s concurrency methods compare, including threading, asyncio, and multiprocessing
- When to use concurrency in your program and which module to use
  

## What Is Concurrency?
The dictionary definition of concurrency is simultaneous occurrence. In Python, the things that are occurring simultaneously are called by different names (**thread, task, process**) but at a high level, they all refer to a sequence of instructions that run in order

Now let’s talk about the simultaneous part of that definition. You have to be a little careful because, when you get down to the details, only `multiprocessing` actually runs these trains of thought at literally the same time. 

`Threading` and `asyncio` both run on a single processor and therefore only run one at a time. They just cleverly find ways to take turns to speed up the overall process. Even though they don’t run different trains of thought simultaneously, we still call this concurrency.

The way the threads or tasks **take turns** is the big difference between `threading` and `asyncio`. 

- In `threading` the operating system actually knows about each thread and can interrupt it at any time to start running a different thread. This is called pre-emptive multitasking since the operating system can pre-empt your thread to make the switch.
https://en.wikipedia.org/wiki/Preemption_%28computing%29#Preemptive_multitasking


Pre-emptive multitasking is handy in that the code in the thread doesn’t need to do anything to make the switch. It can also be difficult because of that “at any time” phrase. This switch can happen in the middle of a single Python statement, even a trivial one like x = x + 1.

- `Asyncio`, on the other hand, uses cooperative multitasking. The tasks must cooperate by announcing when they are ready to be switched out. That means that the code in the task has to change slightly to make this happen.
https://en.wikipedia.org/wiki/Cooperative_multitasking

## What Is Parallelism?

So far, you’ve looked at concurrency that happens on a single processor. What about all of those CPU cores your cool, new laptop has? How can you make use of them? **multiprocessing** is the answer.

With `multiprocessing`, Python creates new processes. A process here can be thought of as almost a completely different program, though technically they’re usually defined as a collection of resources where the resources include memory, file handles and things like that. One way to think about it is that each process runs in *its own Python interpreter*.

Because they are different processes, each of your trains of thought in a multiprocessing program can run on a different core. Running on a different core means that they actually can run at the same time, which is fabulous. There are some complications that arise from doing this, but Python does a pretty good job of smoothing them over most of the time.

Now that you have an idea of what concurrency and parallelism are, let’s review their differences, and then we can look at why they can be useful:

|Concurrency Type   | Switching Decision    | Number of Processors  |
| ----------------- |:---------------------:| ---------------------:|
|Pre-emptive multitasking (threading)	| The operating system decides when to switch tasks external to Python.	| 1 |
|Cooperative multitasking (asyncio)	    | The tasks decide when to give up control.	                            | 1 |
|Multiprocessing (multiprocessing)	    | The processes all run at the same time on different processors.	    | Many |


Each of these types of concurrency can be useful. Let’s take a look at what types of programs they can help you speed up.

## When Is Concurrency Useful?
Concurrency can make a big difference for two types of problems. These are generally called **CPU-bound** and **I/O-bound**.

I/O-bound problems cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource. They arise frequently when your program is working with things that are much slower than your CPU.

Examples of things that are slower than your CPU are legion, but your program thankfully does not interact with most of them. The slow things your program will interact with most frequently are the **file system** and **network connections**.

Let’s see what that looks like:

Timing Diagram of an I/O Bound Program

![alt text](https://files.realpython.com/media/IOBound.4810a888b457.png)

In the diagram above, the blue boxes show time when your program is doing work, and the red boxes are time spent waiting for an I/O operation to complete. This diagram is not to scale because requests on the internet can take several orders of magnitude longer than CPU instructions, so your program can end up spending most of its time waiting. This is what your browser is doing most of the time.

On the flip side, there are classes of programs that do significant computation without talking to the network or accessing a file. These are the CPU-bound programs, because the resource limiting the speed of your program is the CPU, not the network or the file system.

Here’s a corresponding diagram for a CPU-bound program:
![alt text](https://files.realpython.com/media/CPUBound.d2d32cb2626c.png)

As you work through the examples in the following section, you’ll see that different forms of concurrency work better or worse with CPU-bound and I/O-bound programs. Adding concurrency to your program adds extra code and complications, so you’ll need to decide if the potential speed up is worth the extra effort. By the end of this article, you should have enough info to start making that decision.

Here’s a quick summary to clarify this concept:

| I/O-Bound Process	| CPU-Bound Process |
| ----------------- | ----------------- |
|Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer. | You program spends most of its time doing CPU operations. |
| Speeding it up involves overlapping the times spent waiting for these devices. | Speeding it up involves finding ways to do more computations in the same amount of time.

## How to Speed Up an I/O-Bound Program

Let’s start by focusing on I/O-bound programs and a common problem: downloading content over the network. For our example, you will be downloading web pages from a few sites, but it really could be any network traffic. It’s just easier to visualize and set up with web pages.

### Synchronous Version

We’ll start with a non-concurrent version of this task. Note that this program requires the `requests` module. You should run pip install requests before running it, probably using a virtualenv. This version does not use concurrency at all:
(see `01_io_bound_non_concurrent.py`)

As you can see, this is a fairly short program. download_site() just downloads the contents from a URL and prints the size. One small thing to point out is that we’re using a Session object from requests.

It is possible to simply use get() from requests directly, but creating a Session object allows requests to do some fancy networking tricks and really speed things up.

download_all_sites() creates the Session and then walks through the list of sites, downloading each one in turn. Finally, it prints out how long this process took so you can have the satisfaction of seeing how much concurrency has helped us in the following examples.

The processing diagram for this program will look much like the I/O-bound diagram in the last section.

**
Note: Network traffic is dependent on many factors that can vary from second to second. I’ve seen the times of these tests double from one run to another due to network issues.
**

### Why the Synchronous Version Rocks

The great thing about this version of code is that, well, it’s easy. It was comparatively easy to write and debug. It’s also more straight-forward to think about. There’s only one train of thought running through it, so you can predict what the next step is and how it will behave.

### The Problems With the Synchronous Version

The big problem here is that it’s relatively slow compared to the other solutions we’ll provide. Here’s an example of what the final output gave on my machine:

Being slower isn’t always a big issue, however. If the program you’re running takes only 2 seconds with a synchronous version and is only run rarely, it’s probably not worth adding concurrency. You can stop here.

*What if your program is run frequently? What if it takes hours to run? Let’s move on to concurrency by rewriting this program using threading.*

### `threading` Version
As you probably guessed, writing a threaded program takes more effort. You might be surprised at how little extra effort it takes for simple cases, however. Here’s what the same program looks like with `threading`
( see `02_io_bound_threading.py`)

When you add threading, the overall structure is the same and you only needed to make a few changes. download_all_sites() changed from calling the function once per site to a more complex structure.

In this version, you’re creating a `ThreadPoolExecutor`, which seems like a complicated thing. Let’s break that down: **ThreadPoolExecutor = Thread + Pool + Executor**.

You already know about the Thread part. That’s just a train of thought we mentioned earlier. The Pool portion is where it starts to get interesting. This object is going to create a pool of threads, each of which can run concurrently. Finally, the Executor is the part that’s going to control how and when each of the threads in the pool will run. It will execute the request in the pool.

Helpfully, the standard library implements ThreadPoolExecutor as a context manager so you can use the with syntax to manage creating and freeing the pool of Threads.

Once you have a ThreadPoolExecutor, you can use its handy .map() method. This method runs the passed-in function on each of the sites in the list. The great part is that it automatically runs them concurrently using the pool of threads it is managing.

Those of you coming from other languages, or even Python 2, are probably wondering where the usual objects and functions are that manage the details you’re used to when dealing with threading, things like Thread.start(), Thread.join(), and Queue.

These are all still there, and you can use them to achieve fine-grained control of how your threads are run. But, starting with Python 3.2, the standard library added a higher-level abstraction called Executors that manage many of the details for you if you don’t need that fine-grained control.

The other interesting change in our example is that each thread needs to create its own requests.Session() object. When you’re looking at the documentation for requests, it’s not necessarily easy to tell, but reading this issue, it seems fairly clear that you need a separate Session for each thread.

This is one of the interesting and difficult issues with threading. Because the operating system is in control of when your task gets interrupted and another task starts, any data that is shared between the threads needs to be protected, or thread-safe. Unfortunately requests.Session() is not thread-safe.

There are several strategies for making data accesses thread-safe depending on what the data is and how you’re using it. One of them is to use thread-safe data structures like Queue from Python’s queue module.

These objects use low-level primitives like threading.Lock to ensure that only one thread can access a block of code or a bit of memory at the same time. You are using this strategy indirectly by way of the ThreadPoolExecutor object.

Another strategy to use here is something called thread local storage. Threading.local() creates an object that look like a global but is specific to each individual thread. In your example, this is done with threadLocal and get_session():

`ThreadLocal` is in the threading module to specifically solve this problem. It looks a little odd, but you only want to create one of these objects, not one for each thread. The object itself takes care of separating accesses from different threads to different data.

When get_session() is called, the session it looks up is specific to the particular thread on which it’s running. So each thread will create a single session the first time it calls get_session() and then will simply use that session on each subsequent call throughout its lifetime.

Finally, a quick note about picking the number of threads. You can see that the example code uses 5 threads. Feel free to play around with this number and see how the overall time changes. You might expect that having one thread per download would be the fastest but, at least on my system it was not. I found the fastest results somewhere between 5 and 10 threads. If you go any higher than that, then the extra overhead of creating and destroying the threads erases any time savings.

The difficult answer here is that the correct number of threads is not a constant from one task to another. Some experimentation is required

### Why the threading Version Rocks

It’s fast! Here’s the fastest run of my tests. Remember that the non-concurrent version took more than 14 seconds:

Here’s what its execution timing diagram looks like:
![alt text](https://files.realpython.com/media/Threading.3eef48da829e.png)

It uses multiple threads to have multiple open requests out to web sites at the same time, allowing your program to overlap the waiting times and get the final result faster! Yippee! That was the goal.

### The Problems with the threading Version

Well, as you can see from the example, it takes a little more code to make this happen, and you really have to give some thought to what data is shared between threads.

Threads can interact in ways that are subtle and hard to detect. These interactions can cause race conditions that frequently result in random, intermittent bugs that can be quite difficult to find. Those of you who are unfamiliar with the concept of race conditions might want to expand and read the section below.

**RACE CONDITION**
Race conditions are an entire class of subtle bugs that can and frequently do happen in multi-threaded code. Race conditions happen because the programmer has not sufficiently protected data accesses to prevent threads from interfering with each other. You need to take extra steps when writing threaded code to ensure things are thread-safe.

What’s going on here is that the operating system is controlling when your thread runs and when it gets swapped out to let another thread run. This thread swapping can occur at any point, even while doing sub-steps of a Python statement. As a quick example, look at this function:
(see `03_race_condition_ex.py`)

### `asyncio` Version

Before you jump into examining the asyncio example code, let’s talk more about how asyncio works.

**asyncio Basics**

...


### async and await


## `multiprocessing` Version

Unlike the previous approaches, the multiprocessing version of the code takes full advantage of the multiple CPUs that your cool, new computer has. Or, in my case, that my clunky, old laptop has. Let’s start with the code

This is much shorter than the asyncio example and actually looks quite similar to the threading example, but before we dive into the code, let’s take a quick tour of what multiprocessing does for you.

### multiprocessing in a Nutshell

Up until this point, all of the examples of concurrency in this article run only on a single CPU or core in your computer. The reasons for this have to do with the current design of CPython and something called the Global Interpreter Lock, or GIL.

This article won’t dive into the hows and whys of the GIL. It’s enough for now to know that the synchronous, threading, and asyncio versions of this example all run on a single CPU.

`multiprocessing` in the standard library was designed to break down that barrier and run your code across multiple CPUs. At a high level, it does this by creating a new instance of the Python interpreter to run on each CPU and then farming out part of your program to run on it.

As you can imagine, bringing up a separate Python interpreter is not as fast as starting a new thread in the current Python interpreter. It’s a heavyweight operation and comes with some restrictions and difficulties, but for the correct problem, it can make a huge difference.

### multiprocessing Code

The code has a few small changes from our synchronous version. The first one is in download_all_sites(). Instead of simply calling download_site() repeatedly, it creates a multiprocessing.Pool object and has it map download_site to the iterable sites. This should look familiar from the threading example.

What happens here is that the Pool creates a number of separate Python interpreter processes and has each one run the specified function on some of the items in the iterable, which in our case is the list of sites. The communication between the main process and the other processes is handled by the multiprocessing module for you.

The line that creates Pool is worth your attention. First off, it does not specify how many processes to create in the Pool, although that is an optional parameter. By default, multiprocessing.Pool() will determine the number of CPUs in your computer and match that. This is frequently the best answer, and it is in our case.

For this problem, increasing the number of processes did not make things faster. It actually slowed things down because the cost for setting up and tearing down all those processes was larger than the benefit of doing the I/O requests in parallel.

Next we have the initializer=set_global_session part of that call. Remember that each process in our Pool has its own memory space. That means that they cannot share things like a Session object. You don’t want to create a new Session each time the function is called, you want to create one for each process.

The initializer function parameter is built for just this case. There is not a way to pass a return value back from the initializer to the function called by the process download_site(), but you can initialize a global session variable to hold the single session for each process. Because each process has its own memory space, the global for each one will be different.

That’s really all there is to it. The rest of the code is quite similar to what you’ve seen before.

Why the multiprocessing Version Rocks

The multiprocessing version of this example is great because it’s relatively easy to set up and requires little extra code. It also takes full advantage of the CPU power in your computer. The execution timing diagram for this code looks like this:


