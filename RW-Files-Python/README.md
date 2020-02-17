That's all folk !!!


https://realpython.com/read-write-files-python/

https://realpython.com/python-csv/
https://realpython.com/working-with-large-excel-files-in-pandas/

https://realpython.com/python-json/



## Line Endings
One problem often encountered when working with file data is the representation of a new line or line ending. The line ending has its roots from back in the Morse Code era, when a specific pro-sign was used to communicate the end of a transmission or the end of a line.

Later, this was standardized for teleprinters by both the International Organization for Standardization (ISO) and the American Standards Association (ASA). ASA standard states that line endings should use the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n). The ISO standard however allowed for either the CR+LF characters or just the LF character.

Windows uses the CR+LF characters to indicate a new line, while Unix and the newer Mac versions use just the LF character. This can cause some complications when you’re processing files on an operating system that is different than the file’s source. Here’s a quick example. Let’s say that we examine the file dog_breeds.txt that was created on a Windows system:


There are three different categories of file objects:

1. Text files

```python
open('abc.txt')

open('abc.txt', 'r')

open('abc.txt', 'w')
```

With these types of files, open() will return a TextIOWrapper file object:

```python
file = open('dog_breeds.txt')
type(file)
```

2. Buffered binary files
```python

open('abc.txt', 'rb')

open('abc.txt', 'wb')
```

With these types of files, open() will return either a BufferedReader or BufferedWriter file object:

```python
file = open('dog_breeds.txt', 'rb')
type(file)
<class '_io.BufferedReader'>

file = open('dog_breeds.txt', 'wb')
type(file)
<class '_io.BufferedWriter'>
```

3. Raw binary files
```python
open('abc.txt', 'rb', buffering=0)
```

With these types of files, open() will return a FileIO file object:

```python
file = open('dog_breeds.txt', 'rb', buffering=0)
type(file)
```

## Reading

|Method	|               What It Does        |
| ----- | --------------------------------- |
| .read(size=-1)        | This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
| .readline(size=-1)	| This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
| .readlines()	        | This reads the remaining lines from the file object and returns them as a list.


## Writing

|Method	|               What It Does        |
| ----- | --------------------------------- |
| .write(string)    | This writes the string to the file.
| .writelines(seq)  | This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).


## Creating Your Own Context Manager
There may come a time when you’ll need finer control of the file object by placing it inside a custom class. When you do this, using the with statement can no longer be used unless you add a few magic methods: `__enter__` and `__exit__`. By adding these, you’ll have created what’s called a context manager.

`__enter__()` is invoked when calling the with statement. `__exit__()` is called upon exiting from the with statement block.

Here’s a template that you can use to make your custom class:

```python
class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    # Additional methods implemented below
```

Now that you’ve got your custom class that is now a context manager, 
you can use it similarly to the `open()` built-in:

```python
with my_file_reader('dog_breeds.txt') as reader:
    # Perform custom class operations
    pass
```



Here’s a good example. Remember the cute Jack Russell image we had? Perhaps you want to open other .png files but don’t want to parse the header file each time. Here’s an example of how to do this. This example also uses custom iterators. If you’re not familiar with them, check out Python Iterators:

https://dbader.org/blog/python-iterators


```python
class PngReader():
    # Every .png file contains this in the header.  Use it to verify
    # the file is indeed a .png.
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    def __init__(self, file_path):
        # Ensure the file has the right extension
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension")
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')

        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The File is not a properly formatted .png file!")

        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        # This and __next__() are used to create a custom iterator
        # See https://dbader.org/blog/python-iterators
        return self

    def __next__(self):
        # Read the file in "Chunks"
        # See https://en.wikipedia.org/wiki/Portable_Network_Graphics#%22Chunks%22_within_the_file

        initial_data = self.__file_object.read(4)

        # The file hasn't been opened or reached EOF.  This means we
        # can't go any further so stop the iteration by raising the
        # StopIteration.
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            # Each chunk has a len, type, data (based on len) and crc
            # Grab these values and return them as a tuple
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc
```

You can now open .png files and properly parse them using your custom context manager:

```python
with PngReader('jack_russell.png') as reader:
    for l, t, d, c in reader:
        print(f"{l:05}, {t}, {c}")
```

