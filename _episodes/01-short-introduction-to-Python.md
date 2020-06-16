---
title: Short Introduction to Programming in Python
teaching: 30
exercises: 0
questions:
    - "What is Python?"
    - "Why should I learn Python?"
objectives:
    - "Describe the advantages of using programming vs. completing repetitive tasks by hand."
    - "Define the following data types in Python: strings, integers, and floats."
    - "Perform mathematical operations in Python using basic operators."
    - "Define the following as it relates to Python: lists, tuples, and dictionaries."
keypoints:
    - "Python is an interpreted language which can be used interactively (executing one command at a time) or in scripting mode (executing a series of commands saved in file)."
    - "One can assign a value to a variable in Python. Those variables can be of several types, such as string, integer, floating point and complex numbers."
    - "Lists and tuples are similar in that they are ordered lists of elements; they differ in that a tuple is immutable (cannot be changed)."
    - "Dictionaries are data structures that provide mappings between keys and values."
---

## Interpreter

Python is an interpreted language which can be used in two ways:

* "Interactively": when you use it as an "advanced calculator" executing
  one command at a time. To start Python in this mode, execute `python`
  on the command line:

~~~
$ python
~~~
{: .language-bash}

~~~
Python 3.5.1 (default, Oct 23 2015, 18:05:06)
[GCC 4.8.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~
{: .output}

Chevrons `>>>` indicate an interactive prompt in Python, meaning that it is waiting for your
input.

~~~
2 + 2
~~~
{: .language-python}

~~~
4
~~~
{: .output}

~~~
print("Hello World")
~~~
{: .language-python}
~~~
Hello World
~~~
{: .output}

* "Scripting" Mode: executing a series of "commands" saved in text file,
  usually with a `.py` extension after the name of your file:

~~~
$ python my_script.py
~~~
{: .language-bash}

~~~
Hello World
~~~
{: .output}

## Introduction to Python built-in data types

### Strings, integers, and floats

One of the most basic things we can do in Python is assign values to variables:

~~~
text = "Data Carpentry"  # An example of a string
number = 42  # An example of an integer
pi_value = 3.1415  # An example of a float
~~~
{: .language-python}

Here we've assigned data to the variables `text`, `number` and `pi_value`,
using the assignment operator `=`. To review the value of a variable, we
can type the name of the variable into the interpreter and press <kbd>Return</kbd>:

~~~
text
~~~
{: .language-python}
~~~
"Data Carpentry"
~~~
{: .output}

Everything in Python has a type. To get the type of something, we can pass it
to the built-in function `type`:

~~~
type(text)
~~~
{: .language-python}
~~~
<class 'str'>
~~~
{: .output}

~~~
type(number)
~~~
{: .language-python}
~~~
<class 'int'>
~~~
{: .output}

~~~
type(pi_value)
~~~
{: .language-python}
~~~
<class 'float'>
~~~
{: .output}

The variable `text` is of type `str`, short for "string". Strings hold
sequences of characters, which can be letters, numbers, punctuation
or more exotic forms of text (even emoji!).

We can also see the value of something using another built-in function, `print`:

~~~
print(text)
~~~
{: .language-python}
~~~
Data Carpentry
~~~
{: .output}
~~~
print(number)
~~~
{: .language-python}
~~~
42
~~~
{: .output}

This may seem redundant, but in fact it's the only way to display output in a script:

*example.py*
~~~
# A Python script file
# Comments in Python start with #
# The next line assigns the string "Data Carpentry" to the variable "text".
text = "Data Carpentry"

# The next line does nothing!
text

# The next line uses the print function to print out the value we assigned to "text"
print(text)
~~~
{: .language-python}

*Running the script*
~~~
$ python example.py
~~~
{: .language-bash}

~~~
Data Carpentry
~~~
{: .output}

Notice that "Data Carpentry" is printed only once.

**Tip**: `print` and `type` are built-in functions in Python. Later in this
lesson, we will introduce methods and user-defined functions. The Python
documentation is excellent for reference on the differences between them.

### Operators

We can perform mathematical calculations in Python using the basic operators
 `+, -, /, *, %`:

~~~
2 + 2  # Addition
~~~
{: .language-python}

~~~
4
~~~
{: .output}

~~~
6 * 7  # Multiplication
~~~
{: .language-python}
~~~
42
~~~
{: .output}
~~~
2 ** 16  # Power
~~~
{: .language-python}
~~~
65536
~~~
{: .output}
~~~
13 % 5  # Modulo
~~~
{: .language-python}
~~~
3
~~~
{: .output}

We can also use comparison and logic operators:
`<, >, ==, !=, <=, >=` and statements of identity such as
`and, or, not`. The data type returned by this is
called a _boolean_.


~~~
3 > 4
~~~
{: .language-python}
~~~
False
~~~
{: .output}

~~~
True and True
~~~
{: .language-python}
~~~
True
~~~
{: .output}

~~~
True or False
~~~
{: .language-python}
~~~
True
~~~
{: .output}

~~~
True and False
~~~
{: .language-python}
~~~
False
~~~
{: .output}

## Sequences: Lists and Tuples

### Lists

**Lists** are a common data structure to hold an ordered sequence of
elements. Each element can be accessed by an index.  Note that Python
indexes start with 0 instead of 1:

~~~
numbers = [1, 2, 3]
numbers[0]
~~~
{: .language-python}
~~~
1
~~~
{: .output}

A `for` loop can be used to access the elements in a list or other Python data
structure one at a time:

~~~
for num in numbers:
    print(num)
~~~
{: .language-python}

~~~
1
2
3
~~~
{: .output}

**Indentation** is very important in Python. Note that the second line in the
example above is indented. Just like three chevrons `>>>` indicate an
interactive prompt in Python, the three dots `...` are Python's prompt for
multiple lines. This is Python's way of marking a block of code. [Note: you
do not type `>>>` or `...`.]

To add elements to the end of a list, we can use the `append` method. Methods
are a way to interact with an object (a list, for example). We can invoke a
method using the dot `.` followed by the method name and a list of arguments
in parentheses. Let's look at an example using `append`:

~~~
numbers.append(4)
print(numbers)
~~~
{: .language-python}

~~~
[1, 2, 3, 4]
~~~
{: .output}

To find out what methods are available for an
object, we can use the built-in `help` command:

~~~
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
~~~
{: .output}

### Tuples

A **tuple** is similar to a list in that it's an ordered sequence of elements.
However, tuples can not be changed once created (they are "immutable"). Tuples
are created by placing comma-separated values inside parentheses `()`.

~~~
# Tuples use parentheses
a_tuple = (1, 2, 3)
another_tuple = ('blue', 'green', 'red')

# Note: lists use square brackets
a_list = [1, 2, 3]
~~~
{: .language-python}

> ## Tuples _vs._ Lists
> 1. What happens when you execute `a_list[1] = 5`?
> 2. What happens when you execute `a_tuple[2] = 5`?
> 3. What does `type(a_tuple)` tell you about `a_tuple`?
{: .challenge}


## Dictionaries

A **dictionary** is a container that holds pairs of objects - keys and values.

~~~
translation = {'one': 'first', 'two': 'second'}
translation['one']
~~~
{: .language-python}
~~~
'first'
~~~
{: .output}

Dictionaries work a lot like lists - except that you index them with *keys*.
You can think about a key as a name or unique identifier for the value it corresponds to.
~~~
rev = {'first': 'one', 'second': 'two'}
rev['first']
~~~
{: .language-python}
~~~
'one'
~~~
{: .output}

To add an item to the dictionary we assign a value to a new key:

~~~
rev = {'first': 'one', 'second': 'two'}
rev['third'] = 'three'
rev
~~~
{: .language-python}
~~~
{'first': 'one', 'second': 'two', 'third': 'three'}
~~~
{: .output}

Using `for` loops with dictionaries is a little more complicated. We can do
this in two ways:

~~~
for key, value in rev.items():
    print(key, '->', value)
~~~
{: .language-python}

~~~
'first' -> one
'second' -> two
'third' -> three
~~~
{: .output}

or

~~~
for key in rev.keys():
    print(key, '->', rev[key])
~~~
{: .language-python}
~~~
'first' -> one
'second' -> two
'third' -> three
~~~
{: .output}

> ## Changing dictionaries
>
> 1. First, print the value of the `rev` dictionary to the screen.
> 2. Reassign the value that corresponds to the key `second` so that it no longer
>    reads "two" but instead `2`.
> 3. Print the value of `rev` to the screen again to see if the value has changed.
{: .challenge}


## Functions

Defining a section of code as a **function** in Python is done using the `def`
keyword. For example a function that takes two arguments and returns their sum
can be defined as:

~~~
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)
~~~
{: .language-python}
~~~
42
~~~
{: .output}

{% include links.md %}

