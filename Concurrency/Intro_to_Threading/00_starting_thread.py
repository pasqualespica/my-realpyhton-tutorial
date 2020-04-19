import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting sleep...", name)
    time.sleep(2)
    # logging.info("Thread %s: finishing", name)
    logging.info("Thread %s: finishing %s", name, threading.get_ident())



def my_thread_function_2(name, my_nik, my_sleep):
    logging.info("Thread %s: starting `%s` sleep (%d)...", name, my_nik, my_sleep)
    time.sleep(my_sleep)
    logging.info("Thread %s: finishing %s", name, threading.get_ident())


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    
    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=my_thread_function_2, args=(2,"pasqualino", 5))

    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    # y.join()
    logging.info("Main    : all done !!! ")
