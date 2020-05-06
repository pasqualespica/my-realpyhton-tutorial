# grep.py
#
# A very simple coroutine

def grep(pattern):
    print (f"Looking for {pattern}")
    while True:
        line = (yield) # .next() advances the coroutine to the ﬁrst yield expression
        if pattern in line:
            print (line)

# Example use
if __name__ == '__main__':
    g = grep("python")
    next(g)
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
