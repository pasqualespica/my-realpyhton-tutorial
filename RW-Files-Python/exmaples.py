

with open('iris.data', 'r') as reader:
    print("Read & print the entire file")
    print(reader.read())


with open('lorem.txt', 'r') as reader:
    # Read & print the first 5 characters of the line 5 times
    print(reader.readline(5))
    # Notice that line is greater than the 5 chars and continues
    # down the line, reading 5 chars each time until the end of the
    # line and then "wraps" around
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))

print("\n Returns a list object")
f = open('lorem.txt')
print(f.readlines())  # Returns a list object

print("\nIterating Over Each Line in the File- WHILE")

# Iterating Over Each Line in the File
with open('lorem.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()

print("\nIterating Over Each Line in the File- FOR")

with open('lorem.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')
        

# Reading a file a write into other file in reverse order

with open('lorem.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()

with open('lorem_rev.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)

print("\nWorking With Bytes")

with open("lorem.txt", 'rb') as reader:
    print(reader.readline())


# Opening a text file using the b flag isn’t that interesting. 
# Let’s say we have this cute picture of PNG ...

# https://en.wikipedia.org/wiki/Portable_Network_Graphics
print("\nWorking With Bytes - PNG ...")

with open('dogs.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))
    

print("\nTips and Trick.")


# Note: To re-iterate, __file__ returns the path relative to where the initial 
# Python script was called. 
# If you need the full system path, you can use os.getcwd() 
# to get the current working directory of your executing code.


print(f"file name {__file__}")


#  Working With Two Files at the Same Time
d_path = 'lorem.txt'
d_r_path = 'lorem_copy.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
