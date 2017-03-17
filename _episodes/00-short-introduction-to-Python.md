---
title: Short Introduction to Programming in Python
teaching: 0
exercises: 0
questions:
  - "What is Python?"
  - "Why should I learn Python?"
objectives:
  - "Describe the advantages of using programming vs. completing repetitive tasks by hand."
  - "Define the following data types in Python: strings, integers, and floats."
  - "Perform mathematical operations in Python using basic operators."
  - "Define the following as it relates to Python: lists, tuples, and dictionaries."
---

# The Basics of Python

Python is a general purpose programming language that supports rapid development
of scripts and applications.

Python's main advantages:

* Open Source software, supported by Python Software Foundation
* Available on all platforms
* It is a general-purpose programming language
* Supports multiple programming paradigms
* Very large community

## Interpreter

Python is an interpreted language. As a consequence, we can use it in two ways:

* "Interactive" Mode: As an "advanced calculator" e.g. one command at a time:

```python
user:host:~$ python
Python 3.5.1 (default, Oct 23 2015, 18:05:06)
[GCC 4.8.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> print("Hello World")
Hello World
```

* "Scripting" Mode: Executing a series of "commands" saved in text file, usually
with a ".py" extension after the name of your file:

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
using the assignment operator `=`. The variable called `text` is a string which
means it can contain letters and numbers. Notice that in order to define a 
string you need to have quotes around your text. To print out the value 
stored in a variable we can simply type the name of the variable into the 
interpreter:

```python
>>> text
"Data Carpentry"
```

however, in scripts we must use the `print` function:

```python
# Comments start with #
# Next line will print out text
print(text)
"Data Carpentry"
```

### Operators

We can perform mathematical calculations in Python using the basic operators
 `+, -, /, *, %`:

```python
>>> 2 + 2
4
>>> 6 * 7
42
>>> 2 ** 16  # power
65536
>>> 13 % 5  # modulo
3
```

We can also use comparison and logic operators:
`<, >, ==, !=, <=, >=` and statements of identity such as
`and, or, not`. The data type returned by this is 
called a _boolean_.


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

**Lists** are a common data structure to hold an ordered sequence of
elements. Each element can be accessed by an index.  Note that Python
indexes start with 0 instead of 1:

```python
>>> numbers = [1,2,3]
>>> numbers[0]
1
```

A `for` loop can be used to access the elements in a list or other Python data
structure one at a time:

```python
for num in numbers:
    print(num)
1
2
3
```

**Indentation** is very important in Python. Note that the second line in the
example above is indented. This is Python's way of marking a block of code. 

To add elements to the end of a list, we can use the `append` method:

```python
>>> numbers.append(4)
>>> print(numbers)
[1,2,3,4]
```

Methods are a way to interact with an object (a list, for example). We can invoke 
a method using the dot `.` followed by the method name and a list of arguments in parentheses. 
To find out what methods are available for an object, we can use the built-in `help` command:

```python
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

### Tuples

A tuple is similar to a list in that it's an ordered sequence of elements. However,
tuples can not be changed once created (they are "immutable"). Tuples are
created by placing comma-separated values inside parentheses `()`.

```python
# tuples use parentheses
a_tuple= (1,2,3)
another_tuple = ('blue','green','red')
# Note: lists use square brackets
a_list = [1,2,3]
```

### Challenge
1. What happens when you type `a_tuple[2]=5` vs `a_list[1]=5` ?
2. Type `type(a_tuple)` into python - what is the object type?


## Dictionaries

A **dictionary** is a container that holds pairs of objects - keys and values.

```python
>>> translation = {"one" : 1, "two" : 2}
>>> translation["one"]
1
```
Dictionaries work a lot like lists - except that you index them with *keys*. 
You can think about a key as a name for or a unique identifier for a set of values
in the dictionary. Keys can only have particular types - they have to be 
"hashable". Strings and numeric types are acceptable, but lists aren't.

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
...     print(key, "->", value)
...
1 -> one
2 -> two
3 -> three
```

or

```python
>>> for key in rev.keys():
...     print(key, "->", rev[key])
...
1 -> one
2 -> two
3 -> three
>>>
```

### Challenge

Can you do reassignment in a dictionary? Give it a try. 

1. First check what `rev` is right now (remember `rev` is the name of our dictionary). 
    
    Type:
```python
>>> rev
```

2. Try to reassign the second value (in the *key value pair*) so that it no longer reads "two" but instead reads "apple-sauce". 

3. Now display `rev` again to see if it has changed. 

It is important to note that dictionaries are "unordered" and do not remember the
sequence of their items (i.e. the order in which key:value pairs were added to 
the dictionary). Because of this, the order in which items are returned from loops
over dictionaries might appear random and can even change with time.

## Functions

Defining part of a program in Python as a function is done using the `def`
keyword. For example a function that takes two arguments and returns their sum
can be defined as:

```python
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)
42
```

Key points here:

* definition starts with `def`
* function body is indented
* `return` keyword precedes returned value
