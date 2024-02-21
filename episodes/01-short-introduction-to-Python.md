---
title: Short Introduction to Programming in Python
teaching: 30
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Describe the advantages of using programming vs. completing repetitive tasks by hand.
- Define the following data types in Python: strings, integers, and floats.
- Perform mathematical operations in Python using basic operators.
- Define the following as it relates to Python: lists, tuples, and dictionaries.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I program in Python?
- How can I represent my data in Python?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Interpreter

Python is an interpreted language which can be used in two ways:

- "Interactively": when you use it as an "advanced calculator" executing
  one command at a time. To start Python in this mode, execute `python`
  on the command line:

```bash
$ python
```

```output
Python 3.5.1 (default, Oct 23 2015, 18:05:06)
[GCC 4.8.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Chevrons `>>>` indicate an interactive prompt in Python, meaning that it is waiting for your
input.

```python
2 + 2
```

```output
4
```

```python
print("Hello World")
```

```output
Hello World
```

- "Scripting" Mode: executing a series of "commands" saved in text file,
  usually with a `.py` extension after the name of your file:

```bash
$ python my_script.py
```

```output
Hello World
```

## Introduction to variables in Python

### Assigning values to variables

One of the most basic things we can do in Python is assign values to variables:

```python
text = "Data Carpentry"  # An example of assigning a value to a new text variable,
                         # also known as a string data type in Python
number = 42              # An example of assigning a numeric value, or an integer data type
pi_value = 3.1415        # An example of assigning a floating point value (the float data type)
```

Here we've assigned data to the variables `text`, `number` and `pi_value`,
using the assignment operator `=`. To review the value of a variable, we
can type the name of the variable into the interpreter and press <kbd>Return</kbd>:

```python
text
```

```output
"Data Carpentry"
```

Everything in Python has a type. To get the type of something, we can pass it
to the built-in function `type`:

```python
type(text)
```

```output
<class 'str'>
```

```python
type(number)
```

```output
<class 'int'>
```

```python
type(pi_value)
```

```output
<class 'float'>
```

The variable `text` is of type `str`, short for "string". Strings hold
sequences of characters, which can be letters, numbers, punctuation
or more exotic forms of text (even emoji!).

We can also see the value of something using another built-in function, `print`:

```python
print(text)
```

```output
Data Carpentry
```

```python
print(number)
```

```output
42
```

This may seem redundant, but in fact it's the only way to display output in a script:

*example.py*

```python
# A Python script file
# Comments in Python start with #
# The next line assigns the string "Data Carpentry" to the variable "text".
text = "Data Carpentry"

# The next line does nothing!
text

# The next line uses the print function to print out the value we assigned to "text"
print(text)
```

*Running the script*

```bash
$ python example.py
```

```output
Data Carpentry
```

Notice that "Data Carpentry" is printed only once.

**Tip**: `print` and `type` are built-in functions in Python. Later in this
lesson, we will introduce methods and user-defined functions.
[The Python documentation](https://docs.python.org/3/)
is excellent for reference on the differences between them.

**Tip**: When editing scripts like *example.py*, be careful not to use word
processors such as MS Word, as they may introduce extra information that
confuses Python. In this lesson we will be using either Jupyter notebooks or
the Spyder IDE, and for your everyday work you may also choose any text editor
such as Notepad++, VSCode, Vim, or Emacs.

### Operators

We can perform mathematical calculations in Python using the basic operators
`+, -, /, *, %`:

```python
2 + 2  # Addition
```

```output
4
```

```python
6 * 7  # Multiplication
```

```output
42
```

```python
2 ** 16  # Power
```

```output
65536
```

```python
13 % 5  # Modulo
```

```output
3
```

We can also use comparison and logic operators:
`<, >, ==, !=, <=, >=` and statements of identity such as
`and, or, not`. The data type returned by this is
called a *boolean*.

```python
3 > 4
```

```output
False
```

```python
True and True
```

```output
True
```

```python
True or False
```

```output
True
```

```python
True and False
```

```output
False
```

## Sequences: Lists and Tuples

### Lists

**Lists** are a common data structure to hold an ordered sequence of
elements. Each element can be accessed by an index.  Note that Python
indexes start with 0 instead of 1:

```python
numbers = [1, 2, 3]
numbers[0]
```

```output
1
```

A `for` loop can be used to access the elements in a list or other Python data
structure one at a time:

```python
for num in numbers:
    print(num)
```

```output
1
2
3
```

**Indentation** is very important in Python. Note that the second line in the
example above is indented. Just like three chevrons `>>>` indicate an
interactive prompt in Python, the three dots `...` are Python's prompt for
multiple lines. This is Python's way of marking a block of code. [Note: you
do not type `>>>` or `...`.]

To add elements to the end of a list, we can use the `append` method. Methods
are a way to interact with an object (a list, for example). We can invoke a
method using the dot `.` followed by the method name and a list of arguments
in parentheses. Let's look at an example using `append`:

```python
numbers.append(4)
print(numbers)
```

```output
[1, 2, 3, 4]
```

To find out what methods are available for an
object, we can use the built-in `help` command:

```output
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

### Tuples

A **tuple** is similar to a list in that it's an ordered sequence of elements.
However, tuples can not be changed once created (they are "immutable"). Tuples
are created by placing comma-separated values inside parentheses `()`.

```python
# Tuples use parentheses
a_tuple = (1, 2, 3)
another_tuple = ('blue', 'green', 'red')

# Note: lists use square brackets
a_list = [1, 2, 3]
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Tuples *vs.* Lists

1. What happens when you execute `a_list[1] = 5`?
2. What happens when you execute `a_tuple[2] = 5`?
3. What does `type(a_tuple)` tell you about `a_tuple`?
4. What information does the built-in function `len()` provide?
  Does it provide the same information on both tuples and lists?
  Does the `help()` function confirm this?

::::::::::::::::::::::::::: solution

1. What happens when you execute `a_list[1] = 5`?

The second value in `a_list` is replaced with `5`.

2. What happens when you execute `a_tuple[2] = 5`?

```error
TypeError: 'tuple' object does not support item assignment
```

As a tuple is immutable, it does not support item assignment. 
Elements in a list can be altered individually.

3. What does `type(a_tuple)` tell you about `a_tuple`?

```output
<class 'tuple'>
```

The function tells you that the variable `a_tuple` is an object of the class `tuple`.

4. What information does the built-in function `len()` provide?
  Does it provide the same information on both tuples and lists?
  Does the `help()` function confirm this?

```python
len(a_list)
```

```output
3
```

```python
len(a_tuple)
```

```output
3
```

`len()` tells us the length of an object.
It works the same for both lists and tuples, 
providing us with the number of entries in each case.

```python
help(len)
```

```output
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

Lists and tuples are both types of container 
i.e. objects that can contain multiple items,
the key difference being that lists are mutable i.e.
they can be modified after they have been created,
while tuples are not: their value cannot be modified, only overwritten.

::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Dictionaries

A **dictionary** is a container that holds pairs of objects - keys and values.

```python
translation = {'one': 'first', 'two': 'second'}
translation['one']
```

```output
'first'
```

Dictionaries work a lot like lists - except that you index them with *keys*.
You can think about a key as a name or unique identifier for the value it corresponds to.

```python
rev = {'first': 'one', 'second': 'two'}
rev['first']
```

```output
'one'
```

To add an item to the dictionary we assign a value to a new key:

```python
rev['third'] = 'three'
rev
```

```output
{'first': 'one', 'second': 'two', 'third': 'three'}
```

Using `for` loops with dictionaries is a little more complicated. We can do
this in two ways:

```python
for key, value in rev.items():
    print(key, '->', value)
```

```output
'first' -> one
'second' -> two
'third' -> three
```

or

```python
for key in rev.keys():
    print(key, '->', rev[key])
```

```output
'first' -> one
'second' -> two
'third' -> three
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Changing dictionaries

1. First, print the value of the `rev` dictionary to the screen.
2. Reassign the value that corresponds to the key `second` so that it no longer
  reads "two" but instead `2`.
3. Print the value of `rev` to the screen again to see if the value has changed.
  
::::::::::::::::::::::::::: solution

1.

```python
print(rev)
```

```output
{'first': 'one', 'second': 'two', 'third': 'three'}
```

2. and 3.

```python
rev['second'] = 2
print(rev)
```

```output
{'first': 'one', 'second': 2, 'third': 'three'}
```

::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: instructor

## Assigning to Dictionaries

It can help to further demonstrate the freedom the user has to define
values to keys in a dictionary, by showing another example with a value
completely unrelated to the current contents of the dictionary, e.g.

```python
rev[2] = "apple-sauce"
print(rev)
```

```output
{1: 'one', 2: 'apple-sauce', 3: 'three'}
```

:::::::::::::::::::::::::::::::::::

## Functions

Defining a section of code as a **function** in Python is done using the `def`
keyword. For example a function that takes two arguments and returns their sum
can be defined as:

```python
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)
```

```output
42
```



:::::::::::::::::::::::::::::::::::::::: keypoints

- Python is an interpreted language which can be used interactively (executing one command at a time) or in scripting mode (executing a series of commands saved in file).
- One can assign a value to a variable in Python. Those variables can be of several types, such as string, integer, floating point and complex numbers.
- Lists and tuples are similar in that they are ordered lists of elements; they differ in that a tuple is immutable (cannot be changed).
- Dictionaries are data structures that provide mappings between keys and values.

::::::::::::::::::::::::::::::::::::::::::::::::::


