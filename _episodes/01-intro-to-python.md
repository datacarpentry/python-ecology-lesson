---
title: Introduction to python
teaching: 50
exercises: 30
questions:
  - "How can I do basic calculations in python?"
  - "How can I use functions in python?"
  - "What data types are there?"
objectives:
- "Define the following terms as they relate to python: variables, objects, assign, call, function, arguments, options, attributes, methods."
- "Create variables and and assign values to them."
- "Use comments to inform scripts."
- "Do simple arithmetic operations in python using values and variables."
- "Call functions and use arguments to change their default options."
- "Use built in and third party modules/libraries in python."
- "Define the following data types in python: strings, integers, floats, lists, and numpy arrays."
- "Create and manipulate lists and numpy arrays."
- "Subset and extract values from lists and arrays."
- "Use attributes and methods with lists and arrays."
- "Correctly define and handle missing values." 
keypoints: 
- the console works like a fancy calculator
- naming variables in python should be consistent, there are style files that can be followed
- assigning a value to one variable does not change the values of other variables
- functions have one or more arguments, some of them can be optional
- modules increase the functionality of python
- python knows numerical, text and logical data types
- lists and numpy arrays are versatile data structures in python
- subsetting uses square brackets and indexing starts at 0
---


# Introduction to python
 ***Data Carpentry contributors***

## Creating variables in python

You can get output from python simply by typing math in the console:

```
3 + 5
12 / 7
```

However, to do useful and interesting things, we need to assign values to _variables_ (or link _objects_ to names/variables). A _variable_ is just a name for a value. Python's _variables_ must begin with a letter and are case sensitive. To create a variable, we need to give it a name followed by an `=` and the value we want to give it:

```
weight_kg = 55
```

`=` is the assignment operator. It assigns values on the right to variables/names on the left. So, after executing `x = 3`, the value of `x` is `3`. Assignments can be done on more than one variable "simultaneously" on the same line like this:

```
a, b = 3, 4
```

Variables can be given any name such as `x`, `current_temperature`, or
`subject_id`. You want your variable names to be explicit and not too long. They cannot start with a number (`2x` is not valid, but `x2` is). Python is case sensitive (e.g., `weight_kg` is different from `Weight_kg`). There are some names that cannot be used because they are the names of fundamental functions in python (e.g., `if`, `else`, `for`,
see [here](https://docs.python.org/2.5/ref/keywords.html) for a complete list). In general, even if it's allowed, it's best to not use other function names (e.g., `list`, `mean`, `data`, `len`). If in doubt, check the help to see if the name is already in use. It's also not allowd to use a dot or minus (`.`, `-`) within a variable name as in `my.dataset` or `my-dataset`. 
It is also recommended to use _nouns_ for variable names, and _verbs_ for function names. It's important to be consistent in the styling of your
code (where you put spaces, how you name variables, etc.). A speciality of python is [indentation](https://docs.python.org/3/reference/lexical_analysis.html#indentation), which is used to define code blocks and consequently structures a program. While this is generally a good style for program code, in the case of python, it is a language requirement. Using a consistent coding style makes your code clearer to read for your future self and your collaborators. There are several style guides for python, e.g. [python's PEP 8](https://www.python.org/dev/peps/pep-0008/), [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), and [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/). 
### Comments
It is useful to leave notes, and explanations in your scripts.
The comment character in python is `#`, anything to the right of a `#` in a script will be ignored by python. 

Just remember how we assigned a value to `weight_kg`:

```
weight_kg = 55
```

Now that python has `weight_kg` in memory, we can do arithmetic with it. We can perform mathematical calculations in python using the basic operators
 `+, -, /, *, %` (plus, subtract, divide, multiply and modulus). For instance, we may want to convert this weight into pounds (weight in pounds is 2.2 times the weight in kg):

```
2.2 * weight_kg
```

We can also change a variable's value by assigning it a new one:

```
weight_kg = 57.5
2.2 * weight_kg
```

This means that assigning a value to one variable does not change the values of other variables.  For example, let's store the animal's weight in pounds in a new variable, `weight_lb`:

```
weight_lb = 2.2 * weight_kg
```

and then change `weight_kg` to 100.

```
weight_kg = 100
```

What do you think is the current content of the object `weight_lb`? 126.5 or 220?


> ## Challenge
>
> What are the values after each statement in the following?
>
> ```
> mass = 47.5            # mass?
> age  = 122             # age?
> mass = mass * 2.0      # mass?
> age  = age - 20        # age?
> mass_index = mass/age  # mass_index?
> ```
{: .challenge}

## Objects vs. variables

Everything in python is an `object`: numbers, lists, functions, even code. A `variable`, as we use the term in Python, is a *way to access* a specific object. It is a binding between a name and an object. 

In python, every object has an ID, a type, and a value. The ID is a unique identifier that identifies a particular instance of an object, the type identifies the class (e.g. integer, string, list) of an object, and the value is the contents of the object. Mutable objects can change their value; immutable objects cannot.

## Functions and their arguments

Functions are "canned scripts" that automate more complicated sets of commands including operations assignments, etc. Many functions are predefined, or can be made available by importing python *modules* (more on that later). A function usually gets one or more inputs called *arguments*. Functions often (but not always) return a *value*. A typical example would be the function `abs()`. The input (the argument) must be a number, and the return value (in fact, the output) is the absolute value of that number. Executing a function ('running it') is called *calling* the function. An example of a function call is:

```
a = -9
b = abs(a)
```

Here, the value of `a` (-9) is given to the `abs()` function, the `abs()` function calculates the absolute value, and returns the value which is then assigned to variable `b`. This function is very simple, because it takes just one argument.

The return 'value' of a function need not be numerical (like that of `abs()`), and it also does not need to be a single item: it can be a set of things, or even a dataset. We'll see that when we read data files into python.

Arguments can be anything, not only numbers or filenames, but also other objects. Exactly what each argument means differs per function, and must be looked up in the documentation (see below). Some functions take arguments which may either be specified by the user, or, if left out, take on a *default* value: these are called *options*. Options are typically used to alter the way the function operates, such as whether it ignores 'bad values', or what symbol to use in a plot.  However, if you want something specific, you can specify a value of your choice which will be used instead of the default.

Let's try a function that can take multiple arguments: `round()`.

```
round(3.14159)
```

Here, we've called `round()` with just one argument, `3.14159`, and it has returned the value `3`.  That's because the default is to round to the nearest whole number. If we want more digits we can see how to do that by getting information about the `round` function.  We can look at the help for this function using `help(round)`.

```
help(round)
```

We see that if we want a different number of digits, we can type `ndigits=2` or however many we want.

```
round(3.14159, ndigits = 2)
```

If you provide the arguments in the exact same order as they are defined you don't have to name them:

```
round(3.14159, 2)
```

And if you do name the arguments, you can switch their order:

```
round(ndigits = 2, number = 3.14159)
```

It's good practice to put the non-optional arguments (like the number you're
rounding) first in your function call, and to specify the names of all optional arguments.  If you don't, someone reading your code might have to look up the definition of a function with unfamiliar arguments to understand what you're doing.

### Using modules and external libraries with python

The by default available [built-in functions](https://docs.python.org/3/library/functions.html) in python are limited. To get to use more functions for e.g. mathematical operations, *modules* can be used. A module in python contains a set of tools, the functions, that perform tasks on our data. There are a couple of modules that come with the [python standard library](https://docs.python.org/3.6/library/index.html) including for example the `math` module, which provides access to mathematical functions and the `statistics` module for calculations of mathematical statistics.

Modules need to be imported using `import` and their functions can then be used by calling the name of the function together with the module name using the syntax `module_name.function_name`. Adding the module name with a `.` before the function name tells python where to find the function. 
For example the function `sqrt` is part of the module `math` and can be called using `math.sqrt()`:

```
import math
math.sqrt(9)
```

To find out more about an imported module use `help(module)` and to simply show a list of all functions use `dir(module)`, e.g. `dir(math)`.

A big advantage of python is its expandability with external modules (or libraries/packages). Importing a library is like getting a piece of lab equipment out of a storage locker and setting it up on the bench for use in a project.
Once a library is set up, it can be used or called to perform many tasks.

In this workshop we will make use of `numPy`, `pandas`, and `matplotlib` which are all part of the [SciPy ecosystem](https://scipy.org).

When importing libraries we can give them a nickname to shorten the command, e.g. `np` is commonly used as a nickname for the `numpy` module:

```
import numpy as np
np.cos(3.14159)
```

In the example above, we have imported numPy as np. This means we don't have to type out `numpy` each time we call a numPy function. `np.cos` calculates the cosine.

> ## Challenge
> 1. Import numpy, try the function `pi` to represent the number pi (remember you can call the function with `np.pi`). 
> 2. Calculate the sine and cosine of pi. 
> 3. What do `floor` and `ceil` do?
{: .challenge}

## Data types

There are two main types of data that we're exploring in
this lesson: numeric and text data types.

Numeric data types include integers (`int`) and floating point real values (`float`). 
A **floating point** number has decimal points even if that decimal point value is 0. For example: 1.13, 2.0, 1234.345. An **integer** will never have a decimal point. Thus if we wanted to store 1.13 as an integer it would be stored as 1. Similarly, 1234.345 would be stored as 1234. You will often see the data type `Int64` in python which stands for 64 bit integer. The 64
simply refers to the memory allocated to store data in each cell which effectively relates to how many digits it can store in each "cell". Allocating space ahead of time allows computers to optimize storage and processing efficiency. 

Text data type is known as *strings* (`str`) in Python. Strings can contain characters and/or numbers. For example, a string might be a word, a sentence, or several sentences. You can't perform mathematical calculations on a string, even if the string contains numbers. Strings are represented as a sequence of Unicode characters (in the range of U+0000 - U+10FFFF) in Python 3.x and thus are often show as `<U..`, e.g. `<U15`.

Another important data type are booleans (`bool`), i.e. `True` and `False`. Booleans represent the truth values of logic and are useful in conditional expressions, and anywhere else you want to represent the truth or falsity of some condition. `True` and `False` are stored as `1` and `0` in python. 

 
> ## Challenge - playing with data types
> * Define the following variables: 
> `a = 2`, `b = 4.5`, `c = "cat"`, `d = int(4.5)`, `e = float(3)`, `f=bool(true)`, `g=bool(0)`
> * Use the function `type()` to find out which data type each variable corresponds to. 
> As you have seen, we can convert a floating point number to an integer or an integer to a floating point number. Notice that Python by default rounds down when it converts from floating point to integer.
> 
> ```python
	# convert a to integer
	a = 7.83
	int(a)
	7
```
{: .challenge}

### Data structures
#### Lists
Data structures represent data types that can contain more than one value. Lists are the most versatile of python's compound data types. A list contains items separated by commas and enclosed within square brackets (`[]`). For example we can create a list of animal weights and assign it to a new variable `weight_g`:

```
weight_g = [50, 60, 65, 82]
```

A list can also contain strings:

```
animals = ["mouse", "rat", "dog"]
```

The quotes around "mouse", "rat", etc. are essential here. Without the quotes python will assume there are variables called `mouse`, `rat` and `dog`. As these variables don't exist in python's memory, there will be an error message.

Lists in python can also hold items of different data type, i.e. a mix of numbers and strings:

```
streets = ["first", "second", "third", 1, 2, 3]
streets
['first', 'second', 'third', 1, 2, 3]
```

You can use functions with lists, e.g. to get the number of elements in a list, i.e. its length, use `len()`:

```
len(animals)
```

The function `type` indicates the class of a variable, in this case a `list`:

```
type(animals)
```

#### Methods
Objects in python can have `methods`, which allow for changes (mutations) of the object. They are like object specific functions, that is they only work with e.g. a `list` or an `int` whereas normal functions are more general. We call `object methods` by adding the `method` to the `object` using a `.`. For example, you can use the `append()` method to add other values to the end of your list:

```
weight_g.append(90)    # adds 90 to the end of the list
weight_g
[50, 60, 65, 82, 90]
```

or use the `remove()` method to delete the first occurrence of an object from the list:

```
animals.remove("rat")
animals
["mouse", "dog"]
```

When typing `list.` and then using the <kbd>tab</kbd> key a window pops up with all available methods for lists. You can also use `help(list)` or `dir(list)` to get an overview of all methods for lists.

Other built-in data types in python are [`tuples`](https://docs.python.org/3/tutorial/datastructures.html?highlight=tuple#tuples-and-sequences) and [`dictionaries`](https://docs.python.org/3/tutorial/datastructures.html?highlight=tuple#dictionaries).

#### Numpy arrays
As described earlier, external libraries or modules largely extend the functionality of python and they also provide more data structures. In this workshop we will use **numpy arrays** (defined with `np.array`) and **pandas dataframes** (we will discuss those in the next episode).

```
weight_array = np.array([50, 60, 65, 82])
weight_array
array([50, 60, 65, 82])
```

NumPy arrays are multidimensional containers of items of the same type. That is, unlike lists, numpy arrays can only contain e.g. integers/floats or strings, but not both. They allow us to perform batch operations on data without any `for` loops (we will discuss loops in episode 5). This is called _vectorization_ and is something that is not possible on python's lists.

> ## Challenge - lists and numpy arrays
> Create a list, `list1`, with numbers 2, 4, 6, 8 and another list, `list2`,  with letters a, b, c, d. Create two numpy arrays, `array1` and `array2`, with the same content as the `list1` and `list2`, resp. 
> Then do the following operations. __Note: some of the operations will cause error messages, can you find out why?__:
> 
> 1. multiply `list1`, `list2`, `array1`, and `array2` by 2
> 2. add 2 to `list1`, `list2`, `array1`, and `array`
> 3. divide `list1`, `list2`, `array1`, and `array2` by 2
> 4. try `list1 + list2`, `array1 + array2`, `list1 + array1`, `list2 + array1`
> 
> Discuss the different behaviour of lists and numpy arrays with your neighbour.
{: .challenge}

> ## Challenge - data types in arrays
> * We’ve seen that numPy arrays can be of type character, float, integer, and boolean. But what happens if we try to mix these types in a single array?
> <!-- * _Answer_: python implicitly converts them to all be the same type -->
>
> * What will happen in each of these examples? (hint: use method `dtype`
>   to check the data type of your objects):
> 1. `num_char = np.array([1, 2, 3, 'a'])`
> 2. `num_logical = np.array([1, 2, 3, bool('true')])`
> 3. `char_logical = np.array(['a', 'b', 'c', bool('true')])`
> 4. `tricky = np.array([1, 2, 3, '4'])`
>
>
> * Why do you think it happens?
>
> > ## _Answer_: 
> > arrays can be of only one data type. python tries to convert (coerce)
> >  the content of this array to find a "common denominator".
> <!--{: .solution}-->
>
> * You've probably noticed that objects of different types get
>   converted into a single, shared type within a vector. In python, we
>   call converting objects from one type into another type
>   _coercion_. These conversions happen according to a hierarchy,
>   whereby some types get preferentially coerced into other
>   types. Can you draw a diagram that represents the hierarchy of how
>   these data types are coerced?
> 
> > ## _Answer_: 
> > `logical -> numeric -> character <- logical`
> > 
> {: .solution}
{: .challenge}

## Subsetting lists and arrays in python

If we want to extract a value from a list, we must provide an index in square brackets. The index represents the position of the value in our list. For instance:

```
animals = ["mouse", "rat", "dog", "cat"]
animals[0]
'mouse'
# to get the last element
animals[-1]
'cat'
```

Python indices start at 0, that is if you want to access the first element of `animals` you need to type `animals[0]`. Languages in the C family (including C++, Java, Perl, and Python) count from 0 because that's simpler for computers to do.
Programming languages like Fortran, MATLAB, Julia, and R start counting at 1, because that's what human beings typically do.

We can also subset numpy arrays using `[]`, and with arrays we can define several indices at the same time, they need to be given as a list or an array:

```
animals_array = np.array(["mouse", "rat", "dog", "cat"])
```
```
animals_array[2]
'dog'
```
```
animals_array[[0,2]]
array(['mouse', 'dog'], 
      dtype='<U5')
``` 
We can also repeat the indices to create an object with more elements than the original one:

```
more_animals = animals_array[[0, 1, 2, 1, 0, 3]]
```
```
more_animals
array(['mouse', 'rat', 'dog', 'rat', 'mouse', 'cat'], 
      dtype='<U5')
```

### Conditional subsetting of arrays

Another common way of subsetting is by using a logical list or array. TRUE will select the element with the same index, while FALSE will not:

```
weight_g = np.array([21, 34, 39, 54, 55])
```
```
# create an array with logical (boolean) values of same length as weight_g
choice = np.array([True, False, True, True, False], dtype = bool)
```
```
# use array choice to subset weight_g
weight_g[choice]
array([21, 39, 54])
```

Typically, these logical arrays are not typed by hand, but are the output of other functions or logical tests. For instance, if you wanted to select only the values above 50: 

```
weight_g > 50
``` 
will return logicals with TRUE for the indices that meet the condition:

```
array([False, False, False,  True,  True], dtype=bool)
```
so we can use this to select only the values above 50:

```
weight_g[weight_g > 50]
array([54, 55])
```

You can combine multiple tests using `&` (both conditions are true, AND) or `|` (at least one of the conditions is true, OR):

```
weight_g[(weight_g < 30) | (weight_g > 50)]
array([21, 54, 55])
```
```
weight_g[(weight_g >= 30) & (weight_g == 21)]
array([], dtype=int64)  # --> empty array returned
```

Here, `<` stands for “less than”, `>` for “greater than”, `>=` for “greater than or equal to”, and `==` for “equal to”. The double equal sign `==` is a test for numerical equality between the left and right hand sides, and should not be confused with the single `=` sign, which performs variable assignment.


> ## Challenge - subsetting
> Create the following list: 
> `sizes = ['S','M','2XL']`
> 
> 1. Take the first element of `sizes` and put it into a new variable. 
> 
> 2. Add elements to `sizes` so that the list ranges from `XS` to `3XL`, the elements should be in the right order. 
> (Hint: check out the method `.insert(index, value)`)
> 
> ## Challenge (optional)
>
> Can you figure out why `"four" > "five"` returns `TRUE`?
> > ## _Answer_:
> > When using ">" or "<" on strings, python compares their alphabetical order. Here, "four" comes after "five", and therefore is "greater than" it.
> {: .solution}
{: .challenge}

Now, that we have learned how to write scripts and the basics of python's data structures, we are ready to start working with a real dataset, and learn about data frames.
