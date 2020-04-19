import concurrent.futures
import logging
import time


# Unfortunately, ThreadPoolExecutor will hide that exception, 
# and (in the case above) the program terminates with no output. 
# This can be quite confusing to debug at first.

# To try this , remove `other` param from `thread_function`
# you won't see anything to output

def thread_function(name, other):
    # logging.info("Thread %s: starting %s", name , nik_name)
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing %s", name, other)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3), ('a','b','c'))
