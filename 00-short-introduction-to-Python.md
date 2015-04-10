---
layout: lesson
root: .
title: Short Introduction to Programming in Python
---

# The Basics of Python

Python is a general purpose programming language, focused on rapid development
of scripts and applications.

Python's main advantages:

* Open Source software, supported by Python Software Foundation
* Available on all platforms
* "Batteries Included" philosophy - libraries for common tasks available in
  standard installation
* supports multiple programming paradigms
* very large community

## Interpreter

Python is an interpreted language. As a consequence, we can use it in two ways:

* Using interpreter as an "advanced calculator" in interactive mode:

```python
user:host:~$ python
Python 2.7.7 (default, Jun  3 2014, 16:16:56)
[GCC 4.8.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> print "Hello World"
Hello World
```

* Executing programs/scripts saved as a text file, usually with `*.py` extension:

```
user:host:~$ python my_script.py
Hello World
```


## Introduction to Python built-in data types

### Strings, integers and floats

The most basic data types in Python are strings, integers and floats:

```python
text = "Data Carpentry"
number = 42
pi_value = 3.1415
```

Here we've assigned data to variables, namely `text`, `number` and `pi_value`,
using the assignment operator `=`. Python variables don't have to hold specific
data types - we can reassign them - but be careful as this can be confusing.

To print out the value stored in a variable we can simply type the name of the
variable into the interpreter:

```python
>>> text
"Data Carpentry"
```

but this only works in the interpreter. In scripts we must use the `print` command:

```python
# Comments start with #
# Next line will print out text
print text
"Data Carpentry"
```

### Operators

We can do math in Python using the basic operators `+, -, /, *, %`:

```python
>>> 2 + 2
4
>>> 6 * 7
42
>>> 2 ** 16 # power
65536
>>> 3 % 2 # modulo
1
```

We can also use comparison and logic operators:
`<, >, ==, !=, <=, >=` etc.
`and, or, not`

```python
>>> 3 > 4
False
>>> True and True
True
>>> True or False
True
```

## Sequential types: Lists and Tuples

### Lists

**Lists** are the most common data structure that can hold a sequence of
elements. Each element can be accessed by its index:

```python
>>> numbers = [1,2,3]
>>> l[0]
1
```

A `for` loop can be used to access the elements in a sequence one at a time:

```python
for num in numbers:
    print num
1
2
3
```

**Indentation** is very important in Python. Note that second line in above
example is indented - this is Python's way of marking a block of code. We will
discuss this in more detail later.

To add elements to the list, we can use the `append` method:

```python
>>> numbers.append(4)
>>> print numbers
[1,2,3,4]
```

Methods are a way to interact with an object - like a list. Accessing them is
done by using the dot `.`.
To find out what methods are available, we can use the built-in `help` command:

```python
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

or we can get a list of methods by using `dir`. Some methods names are
surrounded by double underscores. Those methods are called "special", and
usually we access them in a different way. For example `__add__` method is
responsible for the `+` operator.

```python
dir(numbers)
>>> dir(numbers)
['__add__', '__class__', '__contains__', ...]
```

### Tuples

A tuple is similar to a list in that it's a sequence of elements. However,
tuples can not be changed once created (they are "immutable"). Tuples are
created by placing comma-separated values inside parentheses `()`.

```python
# tuples use paratheses
ATuple= (1,2,3)
anotherTuple = ('blue','green','red')
# notes lists uses square brackets
AList = [1,2,3]
```

### Challenge
1. What happens when you type `ATuple[2]=5` vs `AList[1]=5` ?
2. Type `type(ATuple)` into python - what is the object type? 


## Dictionaries

A **dictionary** is a container that holds pairs of objects - keys and values.

```python
>>> translation = {"one" : 1, "two" : 2}
>>> translation["one"]
1
```
Dictionaries work a lot like lists - except that you index them with *keys*.
Keys can only have particular types - they have to be "hashable". Strings and
numeric types are acceptable, but lists aren't.

```python
>>> rev = {1 : "one", 2 : "two"}
>>> rev[1]
'one'
>>> bad = {[1,2,3] : 3}
...
TypeError: unhashable type: 'list'
```

To add an item to the dictionary we assign a value to a new key:

```python
>>> rev = {1 : "one", 2 : "two"}
>>> rev[3] = "three"
>>> rev
{1: 'one', 2: 'two', 3: 'three'}
```

Using `for` loops with dictionaries is a little more complicated. We can do this
in two ways:

```python
>>> for key, value in rev.items():
...     print key, "->", value
...
1 -> one
2 -> two
3 -> three
```

or

```python
>>> for key in rev.keys():
...     print key, "->", rev[key]
...
1 -> one
2 -> two
3 -> three
>>>
```

## Functions

Defining part of a program in Python as a function is done using the `def`
keyword. For example a function that takes two arguments and returns their sum
can be defined as:

```python
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print z
42
```

Key points here:

* definition starts with `def`
* function body is indented
* `return` keyword precedes returned value
