# follow.py
#
# A generator that follows a log file like Unix 'tail -f'.
#
# Note: To see this example work, you need to apply to 
# an active server log file.  Run the program "logsim.py"
# in the background to simulate such a file.  This program
# will write entries to a file "access-log".

import time

import time
def follow(thefile):
    # Parameters
    # offset − This is the position of the read/write pointer 
    #           within the file.
    # whence − This is optional and defaults to 0 which means 
    #           absolute file positioning, other values are 1 which means 
    #           seek relative to the current position and 
    #           2 means seek relative to the file's end.

    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         yield line

# Example use
if __name__ == '__main__':
    # logfile = open("access-log")
    logfile = open("/var/log/system.log")
    for line in follow(logfile):
        print(line)
