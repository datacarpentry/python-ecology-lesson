---
layout: lesson
root: ../..
title: Short Introduction to Programming in Python
---

# The Basics of Python

Python is a general purpose programming language, focused on rapid development of scripts and applications.

Python's main advantages:
* Open Source software, supported by Python Software Foundation
* Available on all platforms
* "Batteries Included" philosophy - libraries for common tasks available in standard installation
* supports multiple programming paradigms
* very large community

## Interpreter

Python is interpreted language. As a consequence, we can use it in two ways:
* using interpreter as an "advanced calculator" in interactive mode

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
* executing programs/scripts saved as a text file, usually with `*.py` extension

```
user:host:~$ python my_script.py
Hello World
```

## Introduction to Python build-in data types

### Strings, integers and floats

Most basic data types in Pythons are strings, integers and floats

```python
text = "Data Carpentry"
number = 42
pi_value = 3.1415
```

We assigned data to variables, namely `text`, `number` and `pi_value`, using assign operator `=`. Python variables doesn't hold specific data type - we can reassign them. Be careful - this can be confusing.

To print out the value stored in variable we can simply type them in interpreter

```python
>>> text
"Data Carpentry"
```

but this works only in interperter. In scripts we must use `print` command

```python
# Comments starts with #
# Next line will print out text
print text
"Data Carpentry"
```

### Operators

Python has support for basic operators `+, -, /, *, %`

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

Also comparison and logic operators:
`<, >, ==, !=, <=, >=, etc.`
`and, or, not`

```python
>>> 3 > 4
False
>>> True and True
True
>>> True or False
True
```

## Sequential types: Lists and Dictionaries

### Lists

**List** is most common data structure, that can hold a sequence of elements. Each element can be accessed by it's index:

```python
>>> numbers = [1,2,3]
>>> l[0]
1
```

`for` loop is used to access all the elements in the sequence

```python
for num in numbers:
    print num
1
2
3
```

**Indentations** are very important in Python. Please notice that second line in above example is indented - this is Python way of marking a block of code. We will discuss that in more details later on.

To add elements to the list, we can use method `append`.

```python
>>> numbers.append(4)
>>> print numbers
[1,2,3,4]
```

Methods are the interface of objects - such as lists. Accessing them is done by using dot `.`.
To find out what methods are available, we can use build-in `help` command:

```python
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

or we can get a list of `list` methods by using `dir`. Some methods names are surrounded by double underscores. Those methods are called "special", and usually we access them in a different way. For example `__add__` method is responsible for `+` operator.

```python
dir(numbers)
>>> dir(numbers)
['__add__', '__class__', '__contains__', ...]
```

### Dictionaries

**Dictionary** is a container that keeps pairs of object - key and the value. Usage is really simple

```python
>>> translation = {"one" : 1, "two" : 2}
>>> translation["one"]
1
```

Dictionary works just like a list - except that you can index them with *keys*. There are however limits for keys - they have to be "hashable type". Strings and numeric types are acceptable, but lists aren't.

```python
>>> rev = {1 : "one", 2 : "two"}
>>> rev[1]
'one'
>>> bad = {[1,2,3] : 3}
...
TypeError: unhashable type: 'list'
```

To add an item to the dictionary we assign value to a new key:

```python
>>> rev = {1 : "one", 2 : "two"}
>>> rev[3] = "three"
>>> rev
{1: 'one', 2: 'two', 3: 'three'}
```

Using `for` loop with dictionaries is a little more complicated. We can do it in two ways:
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

Defining part of the program in Python as a function is straightforward. For example a function that takes two arguments and returns sum of them can be defined as:

```python
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print z
42
```

Key points here:
 - definition starts with `def`
 - function body is indented
 - `return` keyword precedes returned value
