import logging
import queue

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=5)

    def get_message(self, name):
        logging.debug("%s:about to get from queue GET ??? ", name)
        value = self.get()
        logging.debug(
            "%s:got %d from queue !!! GET DONE !!! queuesize %d", name, value,
            self.qsize())
        return value

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue PUT ??? ", name, value)
        self.put(value)
        logging.debug("%s:added %d to queue !!! PUT DONE !!! queuesize %d",
                      name, value, self.qsize())
