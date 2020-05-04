# pipeline.py
#
# An example of setting up a processing pipeline with generators

def grep(pattern,lines):
    for line in lines:
        if pattern in line:
             yield line

if __name__ == '__main__':
    from _01_follow import follow

    # Set up a processing pipe : tail -f | grep python
    # logfile  = open("access-log")
    logfile = open("/var/log/system.log")
    loglines = follow(logfile)
    # pylines  = grep("python",loglines)
    pylines = grep("apple", loglines)

    # Pull results out of the processing pipeline
    for line in pylines:
        print(line)
