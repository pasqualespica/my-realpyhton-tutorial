# Speed Up Your Python Program With Concurrency
https://realpython.com/python-concurrency/

https://github.com/realpython/materials/tree/master/concurrency-overview


In this article, you’ll learn the following:

- What concurrency is
- What parallelism is
- How some of Python’s concurrency methods compare, including threading, asyncio, and multiprocessing
- When to use concurrency in your program and which module to use
  

## What Is Concurrency?
The dictionary definition of concurrency is simultaneous occurrence. In Python, the things that are occurring simultaneously are called by different names (thread, task, process) but at a high level, they all refer to a sequence of instructions that run in order

Now let’s talk about the simultaneous part of that definition. You have to be a little careful because, when you get down to the details, only `multiprocessing` actually runs these trains of thought at literally the same time. `Threading` and `asyncio` both run on a single processor and therefore only run one at a time. They just cleverly find ways to take turns to speed up the overall process. Even though they don’t run different trains of thought simultaneously, we still call this concurrency.

The way the threads or tasks **take turns** is the big difference between `threading` and `asyncio`. 

- In `threading` the operating system actually knows about each thread and can interrupt it at any time to start running a different thread. This is called pre-emptive multitasking since the operating system can pre-empt your thread to make the switch.
https://en.wikipedia.org/wiki/Preemption_%28computing%29#Preemptive_multitasking


Pre-emptive multitasking is handy in that the code in the thread doesn’t need to do anything to make the switch. It can also be difficult because of that “at any time” phrase. This switch can happen in the middle of a single Python statement, even a trivial one like x = x + 1.

- `Asyncio`, on the other hand, uses cooperative multitasking. The tasks must cooperate by announcing when they are ready to be switched out. That means that the code in the task has to change slightly to make this happen.
https://en.wikipedia.org/wiki/Cooperative_multitasking
