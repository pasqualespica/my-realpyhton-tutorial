# Async IO in Python: A Complete Walkthrough
https://realpython.com/async-io-python/

### useful links  
https://docs.python.org/3/library/concurrency.html
https://docs.python.org/3/library/asyncio.html

Here’s what you’ll cover:

- Asynchronous IO (async IO): a language-agnostic paradigm (model) that has implementations across a host of programming languages

- async/await: two new Python keywords that are used to define coroutines

- asyncio: the Python package that provides a foundation and API for running and managing coroutines

## Where Does Async IO Fit In?

Concurrency and parallelism are expansive subjects that are not easy to wade into. While this article focuses on async IO and its implementation in Python, it’s worth taking a minute to compare async IO to its counterparts in order to have context about how async IO fits into the larger, sometimes dizzying puzzle.

**Parallelism** consists of performing multiple operations at the same time. `Multiprocessing` is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

**Concurrency** is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

**Threading** is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL, but that’s beyond the scope of this article.

What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.


## The `asyncio` Package and `async/await`

Now that you have some background on async IO as a design, let’s explore Python’s implementation. Python’s `asyncio` package (introduced in Python 3.4) and its two keywords, `async` and `await`, serve different purposes but come together to help you declare, build, execute, and manage asynchronous code.

At the heart of async IO are **coroutines**. A coroutine is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: 
**a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time**



