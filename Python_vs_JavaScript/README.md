
# Python vs JavaScript for Pythonistas

https://realpython.com/python-vs-javascript/



### useful link 

https://webassembly.org/

https://www.w3schools.com/tags/att_script_defer.asp


## W3Schools tutorial 
https://www.w3schools.com/js/


## nodeJS api ( server side )
https://nodejs.org/api/

## React
https://reactjs.org/docs/getting-started.html


## JavaScript Types

In Python, everything is an **object**, whereas JavaScript makes a distinction between **primitive** and **reference types**. They differ in a couple of ways.

*Variables of primitive types are stored in a special memory area called the **stack**, which is fast but has a limited size and is short-lived. Conversely, objects with reference types are allocated on the heap, which is only restricted by the amount of physical memory available on your computer. Such objects have a much longer life cycle but are slightly slower to access.*
https://realpython.com/how-to-implement-python-stack/

These are the only **primitive** types available in JavaScript:

- boolean
- null
- number
- string
- symbol (since ES6)
- undefined

On the other hand, here are a handful of **reference types** that come with JavaScript off the shelf:

- Array
- Boolean
- Date
- Map
- Number
- Object
- RegExp
- Set
- String
- Symbol
- (…)
- 
There’s also a proposal to include a new *BigInt* numeric type,

**autoboxing**

```javascript
> new String('Lorem ipsum').length
11
```

Object is a reference type in JavaScript. Here, you’ve got two variables, x and y, referring to the same instance of a Person object. The change made to one of the variables is reflected in the other variable.

Last but not least, primitive types are **immutable**, which means that you can’t change their state once they are initialized. Every modification, such as incrementing a number or making text uppercase, results in a brand-new copy of the original value. While this is a bit wasteful, there are plenty of good reasons to use immutable values, including thread safety, simpler design, and consistent state management.


---

**Note**: Contrary to Python, multiple inheritance isn’t possible in JavaScript because any given object can have only one prototype. That said, you can use proxy objects, which were introduced in ES6, to mitigate that.
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy

The gist of the story is that there are no classes in JavaScript. Well, technically, you can use the class keyword that was introduced in ES6,

---


**Default Arguments**
Starting with ES6, function arguments can have default values like in Python:

```js
> function greet(name = 'John') {
…   console.log('Hello', name);
… }
> greet();
Hello John
```

**Unlike Python**, however, the default values are resolved every time the function is called instead of only when it’s defined. 
This makes it possible to safely use mutable types as well as to dynamically refer to other arguments passed at runtime:

```js
function foo(a, b=a+1, c=[]) {
    c.push(a);
    c.push(b);
    console.log(c);
    }
foo(1);
foo(5);
```

`JS` result :
```
(base) Pasquales-MacBook-Pro:Implementing-an-Interface-Python pasqualespica$ node
Welcome to Node.js v12.13.0.
Type ".help" for more information.
> function foo(a, b=a+1, c=[]) {
...     c.push(a);
...     c.push(b);
...     console.log(c);
...     }
undefined
> foo(1);
[ 1, 2 ]
undefined
> foo(5);
[ 5, 6 ]
undefined
> 
```

into python instead ...

```python
def foo(a, c=[]):
    c.append(a)
    c.append(a+1)
    print(c)

foo(1)
foo(5)
```

`PYTHON` result :

```
>>> def foo(a, c=[]):
...     c.append(a)
...     c.append(a+1)
...     print(c)
... 
>>> foo(1)
[1, 2]
>>> foo(5)
[1, 2, 5, 6]
>>> 
```


If you know **coroutines** in Python, then you’ll remember that generator objects can be both producers and consumers. You can send arbitrary values into a suspended generator by providing an optional argument to .next():

```js
> function* makeGenerator() {
…   const message = yield 'ping';
…   return message;
… }
> const generator = makeGenerator();
> generator.next();
{value: "ping", done: false}
> generator.next('pong');
{value: "pong", done: true}
```



---
   ``The most challenging part about using DOM is getting skilled at building accurate CSS selectors. You can practice and learn using one of many interactive playgrounds available online.

https://flukeout.github.io/

