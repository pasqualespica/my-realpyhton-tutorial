# Working With JSON Data in Python
https://realpython.com/python-json/


A (Very) Brief History of JSON
Not so surprisingly, JavaScript Object Notation was inspired by a subset of the JavaScript programming language dealing with object literal syntax. They’ve got a nifty website that explains the whole thing. Don’t worry though: JSON has long since become language agnostic and exists as its own standard, so we can thankfully avoid JavaScript for the sake of this discussion.

https://www.json.org/
https://tools.ietf.org/html/rfc8259

```json
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

## Python Supports JSON Natively!
Python comes with a built-in package called json for encoding and decoding JSON data.
https://docs.python.org/3/library/json.html

Just throw this little guy up at the top of your file:
```py
import json
```
## A Little Vocabulary
The process of encoding JSON is usually called **serialization**. This term refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network. You may also hear the term marshaling, but that’s a whole other discussion. Naturally, **deserialization** is the reciprocal process of decoding data that has been stored or delivered in the JSON standard

### Serializing JSON
What happens after a computer processes lots of information? It needs to take a data dump. Accordingly, the `json` library exposes the `dump()` method for writing data to files. There is also a `dumps()` method (pronounced as “dump-s”) for writing to a Python string.

Simple Python objects are translated to JSON according to a fairly intuitive conversion.

|   Python          |	    JSON    |
| ---------         |:-------------:|
| dict	            | object        |
| list, tuple	    | array         |
| str	            | string        |
| int, long, float  | number        |
| True	            | true          |
| False	            | false         |
| None	            | null          |


### A Simple Serialization Example
Imagine you’re working with a Python object in memory that looks a little something like this:
```py
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
```

It is critical that you save this information to disk, so your mission is to write it to a file.

Using Python’s `context manager`, you can create a file called data_file.json and open it in write mode. (JSON files conveniently end in a .json extension.)

```py
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
```

Note that `dump()` takes two positional arguments: 
- (1) the data object to be serialized, and 
- (2) the file-like object to which the bytes will be written.

Or, if you were so inclined as to continue using this serialized JSON data in your program, you could write it to a native Python str object.

```py
json_string = json.dumps(data)
```

### Some Useful Keyword Arguments

The first option most people want to change is whitespace. You can use the indent keyword argument to specify the indentation size for nested structures. Check out the difference for yourself by using data, which we defined above, and running the following commands in a console:

```py
>>> json.dumps(data)
>>> json.dumps(data, indent=4)
```
https://docs.python.org/3/library/json.html#basic-usage

### Deserializing JSON

|   JSON            |	  Python    |
| ---------         |:-------------:|
| object	        | dict          |
| array	            | list          |
| string	        | str           |
| number (int)      | int           |
| number (real)	    | float         |
| true	            | True          |
| false	            | False         |
| null	            | None          |

**hehehehehe :)**

---
*Technically, this conversion isn’t a perfect inverse to the serialization table. That basically means that if you encode an object now and then decode it again later, you may not get exactly the same object back. I imagine it’s a bit like teleportation: break my molecules down over here and put them back together over there. Am I still the same person?*
---

In reality, it’s probably more like getting one friend to translate something into Japanese and another friend to translate it back into English. Regardless, the simplest example would be encoding a tuple and getting back a list after decoding, like so

```py

>>> blackjack_hand = (8, "Q")
>>> encoded_hand = json.dumps(blackjack_hand)
>>> decoded_hand = json.loads(encoded_hand)

>>> blackjack_hand == decoded_hand
False
>>> type(blackjack_hand)
<class 'tuple'>
>>> type(decoded_hand)
<class 'list'>
>>> blackjack_hand == tuple(decoded_hand)
True

```

### A Simple Deserialization Example
This time, imagine you’ve got some data stored on disk that you’d like to manipulate in memory. You’ll still use the context manager, but this time you’ll open up the existing data_file.json in read mode.
```py
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
```
Things are pretty straightforward here, but keep in mind that the result of this method could return any of the allowed data types from the conversion table. This is only important if you’re loading in data you haven’t seen before. In most cases, the root object will be a `dict` or a `list`

If you’ve pulled JSON data in from another program or have otherwise obtained a `string`of JSON formatted data in Python, you can easily deserialize that with `loads()`, which naturally loads from a string:

```py
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
```

### A Real World Example (sort of)
For your introductory example, you’ll use JSONPlaceholder, a great source of fake JSON data for practice purposes.
https://jsonplaceholder.typicode.com/


First create a script file called `scratch.py`, or whatever you want. I can’t really stop you.



### Encoding and Decoding Custom Python Objects
What happens when we try to serialize the Elf class from that Dungeons & Dragons app you’re working on?

```py
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]
```

Not so surprisingly, Python complains that Elf isn’t serializable (which you’d know if you’ve ever tried to tell an Elf otherwise):

```py
>>> elf = Elf(level=4)
>>> json.dumps(elf)
TypeError: Object of type 'Elf' is not JSON serializable
```

Although the `json` module can handle most built-in Python types, it doesn’t understand how to encode customized data types by default. It’s like trying to fit a square peg in a round hole—you need a buzzsaw and parental supervision.


### Simplifying Data Structures
Now, the question is how to deal with more complex data structures. Well, you could try to encode and decode the JSON by hand, but there’s a slightly more clever solution that’ll save you some work. Instead of going straight from the custom data type to JSON, you can throw in an intermediary step.

All you need to do is represent your data in terms of the built-in types json already understands. Essentially, you translate the more complex object into a simpler representation, which the json module then translates into JSON. It’s like the transitive property in mathematics: if A = B and B = C, then A = C.

To get the hang of this, you’ll need a complex object to play with. You could use any custom class you like, but Python has a built-in type called complex for representing complex numbers, and it isn’t serializable by default. So, for the sake of these examples, your complex object is going to be a `complex` object. Confused yet?

```py
>>> z = 3 + 8j
>>> type(z)
<class 'complex'>
>>> json.dumps(z)
TypeError: Object of type 'complex' is not JSON serializable
```

A good question to ask yourself when working with custom types is What is the minimum amount of information necessary to recreate this object? In the case of complex numbers, you only need to know the real and imaginary parts, both of which you can access as attributes on the complex object:

```py
>>> z.real
3.0
>>> z.imag
8.0
```

Passing the same numbers into a complex constructor is enough to satisfy the `__eq__` comparison operator:

```py
>>> complex(3, 8) == z
True
```

### Encoding Custom Types

To translate a custom object into JSON, all you need to do is provide an encoding function to the dump() method’s default parameter. The json module will call this function on any objects that aren’t natively serializable. Here’s a simple decoding function you can use for practice:


```py
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
```

Notice that you’re expected to raise a TypeError if you don’t get the kind of object you were expecting. This way, you avoid accidentally serializing any Elves. Now you can try encoding complex objects for yourself!

```py
>>> json.dumps(9 + 5j, default=encode_complex)
'[9.0, 5.0]'
>>> json.dumps(elf, default=encode_complex)
TypeError: Object of type 'Elf' is not JSON serializable
```

### other common approach FOR not JSON serializable

The other common approach is to subclass the standard JSONEncoder and 
override its `default()` method:

```py
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)
```

Instead of raising the `TypeError` yourself, you can simply let the base class handle it. You can use this either directly in the dump() method via the cls parameter or by creating an instance of the encoder and calling its encode() method:

```py
>>> json.dumps(2 + 5j, cls=ComplexEncoder)
'[2.0, 5.0]'

>>> encoder = ComplexEncoder()
>>> encoder.encode(3 + 6j)
'[3.0, 6.0]'
```

### Decoding Custom Types
While the real and imaginary parts of a complex number are absolutely necessary, they are actually not quite sufficient to recreate the object. This is what happens when you try encoding a complex number with the ComplexEncoder and then decoding the result:

```py
>>> complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
>>> json.loads(complex_json)
[4.0, 17.0]
```

All you get back is a list, and you’d have to pass the values into a complex constructor if you wanted that complex object again. Recall our discussion about teleportation. What’s missing is metadata, or information about the type of data you’re encoding.

I suppose the question you really ought ask yourself is What is the minimum amount of information that is both necessary and sufficient to recreate this object?

The json module expects all custom types to be expressed as objects in the JSON standard. For variety, you can create a JSON file this time called complex_data.json and add the following object representing a complex number:
```json
{
    "__complex__": true,
    "real": 42,
    "imag": 36
}
```

See the clever bit? That "__complex__" key is the metadata we just talked about. It doesn’t really matter what the associated value is. To get this little hack to work, all you need to do is verify that the key exists:
```py
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct
```

If "__complex__" isn’t in the dictionary, you can just return the object and let the default decoder deal with it.

Every time the load() method attempts to parse an object, you are given the opportunity to intercede before the default decoder has its way with the data. You can do this by passing your decoding function to the object_hook parameter.

Now play the same kind of game as before:

```py
>>> with open("complex_data.json") as complex_data:
...     data = complex_data.read()
...     z = json.loads(data, object_hook=decode_complex)
... 
>>> type(z)
<class 'complex'>
```

While `object_hook` might feel like the counterpart to the `dump()` method’s `default` parameter, the analogy really begins and ends there.

This doesn’t just work with one object either. Try putting this list of complex numbers into complex_data.json and running the script again:

```json
[
  {
    "__complex__":true,
    "real":42,
    "imag":36
  },
  {
    "__complex__":true,
    "real":64,
    "imag":11
  }
]
```

If all goes well, you’ll get a list of complex objects:

```py
>>> with open("complex_data.json") as complex_data:
...     data = complex_data.read()
...     numbers = json.loads(data, object_hook=decode_complex)
... 
>>> numbers
[(42+36j), (64+11j)]
```

You could also try subclassing `JSONDecoder` and overriding `object_hook`, but it’s better to stick with the lightweight solution whenever possible.

