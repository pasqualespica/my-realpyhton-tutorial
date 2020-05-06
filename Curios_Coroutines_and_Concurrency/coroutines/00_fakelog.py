#!/Users/pasqualespica/.pyenv/versions/3.8.1/bin/python
import time
import random


# "The optional buffering argument specifies the file’s desired buffer size:"

# 0 means unbuffered,
# 1 means line buffered,
# any other positive value means use a buffer of(approximately) that size.
# A negative buffering means to use the system default, which is usually line buffered for tty devices and fully buffered for other files.
# If omitted, the system default is used.

with open('fake.log', 'w', buffering=1) as writer:
    while True:
        time.sleep(1) # wait 1 sec
        rand_str = "I'm a random number " + str(random.randint(0,1000))
        writer.write(rand_str+"\n")
