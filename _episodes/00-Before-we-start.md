---
title: Before we start
teaching: 30
exercises: 0
questions:
  - "What is Python?"
  - "Why should I learn Python?"
objectives:
- Describe the purpose of the editor, console, help, variable explorer and file explorer panes in Spyder.
- Organize files and directories for a set of analyses as a python/spyder project, and understand the purpose of the working directory.
- Know where to find help
- Demonstrate how to provide sufficient information for troubleshooting with the python user community.
keypoints: 
- python is an open source and platform independent programming language
- the SciPy ecosystem for python provides the tools necessary for scientific computing 
- Spyder is a great IDE to code in and interact with python
- with its large community it is easy to find help in the internet
---

# Before we start
***Data Carpentry contributors***

## What is python? 
Python is a general purpose programming language that supports rapid development of scripts and applications. The term `python` is used to refer to both the programming language and the software that interprets the scripts written using it.

Python's main advantages:

* Open Source software, supported by Python Software Foundation
* Available on all platforms
* It is a general-purpose programming language
* Supports multiple programming paradigms
* Very large community with a rich ecosystem of third-party packages
* interpreted language, i.e. direct execution of commands, no compilation neccessary


## Why learn python for data analysis?
### Python does not involve lots of pointing and clicking, and that’s a good thing
The learning curve might be steeper than with other software, but with python, the results of your analysis does not rely on remembering a succession of pointing and clicking, but instead on a series of written commands, and that’s a good thing! So, if you want to redo your analysis because you collected more data, you don’t have to remember which button you clicked in which order to obtain your results, you just have to run your script again.

Working with scripts makes the steps you used in your analysis clear, and the code you write can be inspected by someone else who can give you feedback and spot mistakes.

Working with scripts forces you to have a deeper understanding of what you are doing, and facilitates your learning and comprehension of the methods you use.

### Python code is great for reproducibility
Reproducibility is when someone else (including your future self) can obtain the same results from the same dataset when using the same analysis.

Python integrates with other tools to generate manuscripts from your code. If you collect more data, or fix a mistake in your dataset, the figures and the statistical tests in your manuscript are updated automatically.

An increasing number of journals and funding agencies expect analyses to be reproducible, so knowing python will give you an edge with these requirements.

### Python is interdisciplinary and extensible
With `numpy`, `pandas`, `sciPy`, `matplotlib` and many other modules that can be installed to extend its capabilities, python provides a framework that allows you to combine approaches from many scientific disciplines to best suit the analytical framework you need to analyze your data. 

#### Scientific Computing Tools for Python - the SciPy ecosystem
To do scientific computions in python, [SciPy](https://scipy.org) offers a collection of open source software for mathematics, science, and engineering:

* [NumPy](http://www.numpy.org), the fundamental package for numerical computation, defines the numerical array and matrix types and basic operations on them. 
* [SciPy](https://scipy.org/scipylib/index.html) is a collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization, statistics and much more.
* [Matplotlib](http://matplotlib.org) is a mature and popular plotting package, that provides publication-quality 2D plotting as well as rudimentary 3D plotting.
* [Pandas](http://pandas.pydata.org) provides high-performance, easy to use data structures.
* [SymPy](http://www.sympy.org/en/index.html) is for symbolic mathematics and computer algebra.

These software can be installed as libraries in python and comes pre-installed with Anaconda. 

### Python works on data of all shapes and sizes
The skills you learn with python scale easily with the size of your dataset. Whether your dataset has hundreds or millions of lines, it won’t make much difference to you.
[pandas](http://pandas.pydata.org), a python data analysis library, comes with special data structures and data types that make handling of missing data and statistical factors convenient.
Python can connect to spreadsheets, databases, and many other data formats, on your computer or on the web.


### Python produces high-quality graphics
The plotting functionalities in python are endless, and allow you to adjust any aspect of your graph to convey most effectively the message from your data. [matplotlib](http://matplotlib.org) is the most popular plotting library in python. 

### Python has a large and welcoming community
Thousands of people use python daily. Many of them are willing to help you through mailing lists and websites such as [Stack Overflow](https://stackoverflow.com), or on the [Anaconda community](https://www.anaconda.com/community/).

### Not only is python free, but it is also open-source and cross-platform
Anyone can inspect the source code to see how python works. Because of this transparency, there is less chance for mistakes, and if you (or someone else) find some, you can report and fix bugs.

## Knowing your way around Anaconda and Spyder

[Spyder](https://spyder-ide.github.io
) is currently a popular way to not only write your python scripts but also to interact with the python software; it is an interactive development enviroment, a so called IDE. To function correctly, Spyder needs python and therefore both need to be installed on your computer. The [Anaconda](https://www.anaconda.com) distribution includes python as well as Spyder and other programs such as the IPython console and Jupyter notebook.

### Getting set up

It is good practice to keep a set of related data, analyses, and text self-contained in a single folder, called the working directory. All of the scripts within this folder can then use relative paths to files that indicate where inside the project a file is located (as opposed to absolute paths, which point to where a file is on a specific computer). Working this way makes it a lot easier to move your project around on your computer and share it with others without worrying about whether or not the underlying scripts will still work.

Spyder provides a helpful set of tools to do this through its “Projects” interface, which not only creates a working directory for you but also remembers its location (allowing you to quickly navigate to it) and optionally preserves custom settings and open files to make it easier to resume work after a break. Below, we will go through the steps for creating an “Python Project” for this tutorial.

* Start _Anaconda Navigator_ and launch _Spyder_ 
* Under the _Projects_ menu, click on _New project_, choose _New directory_
* Enter a name for this new folder (or “directory”), and choose a convenient location for it. This will be your working directory for the rest of the day (e.g., ~/data-carpentry)
* Click on _Create_
* You can customise how Spyder looks like under the _View_ menu, under _Window layouts_ please chose _Spyder Default Layout_, which we want to use for this lesson
* Choose the _Project Explorer_ tab in the top right window of the screen, right click, choose _New_ and _Folder_ and create a folder named data within your newly created working directory (e.g., ~/data-carpentry/data)

### Organizing your working directory
Using a consistent folder structure across your projects will help keep things organized, and will also make it easy to find/file things in the future. This can be especially helpful when you have multiple projects. In general, you may create directories (folders) for scripts, data, and documents.

**`data/`** Use this folder to store your raw data and intermediate datasets you may create for the need of a particular analysis. For the sake of transparency and provenance, you should always keep a copy of your raw data accessible and do as much of your data cleanup and preprocessing as possible programmatically (i.e., with scripts, rather than manually). Separating raw data from processed data is also a good idea. For example, you could have files `data/raw/tree_survey.plot1.txt` and `...plot2.txt` kept separate from a `data/processed/tree.survey.csv` file generated by the `scripts/01.preprocess.tree_survey.py` script.

**`documents/`** This would be a place to keep outlines, drafts, and other text.

**`scripts/`** This would be the location to keep your python scripts for different analyses or plotting, and potentially a separate folder for your functions (more on that later).
You may want additional directories or subdirectories depending on your project needs, but these should form the backbone of your working directory. For this workshop, we will need a `data/` folder to store our raw data, and we will create later a `data_output/` folder when we learn how to export data as CSV files.

## Interacting with Python
The basis of programming is that we write down instructions for the computer to follow, and then we tell the computer to follow those instructions. We write, or code, instructions in python because it is a common language that both the computer and we can understand. We call the instructions commands and we tell the computer to follow the instructions by executing (also called running) those commands.

There are two main ways of interacting with python: by using the console or by using script files (plain text files that contain your code). The console pane (in Spyder, the bottom right panel) is the place where commands written in the python language can be typed and executed immediately by the computer. It is also where the results will be shown for commands that have been executed. You can type commands directly into the console and press Enter to execute those commands, but they will be forgotten when you close the session. Spyder uses the [IPython](http://ipython.org) console by default.

Because we want our code and workflow to be reproducible, it is better to type the commands we want in the script editor, and save the script. This way, there is a complete record of what we did, and anyone (including our future selves!) can easily replicate the results on their computer.

Spyder allows you to execute commands directly from the script editor by using the run buttons on top or keyboard shortcuts. To run the entire script click _Run file_ or press <kbd>F5</kbd>, to run the current line click _Run selection or current line_ or press <kbd>F9</kbd>, other run buttons allow to run script cells or go into debug mode. When using <kbd>F9</kbd>, the command on the current line in the script (indicated by the cursor) or all of the commands in the currently selected text will be sent to the console and executed. 

At some point in your analysis you may want to check the content of a variable or the structure of an object, without necessarily keeping a record of it in your script. You can type these commands and execute them directly in the console. Spyder provides the <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd> and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> shortcuts to allow you to jump between the script and the console panes.

If python is ready to accept commands, the IPython console shows an `In [..]:` prompt with the current console line number in `[]`. If it receives a command (by typing, copy-pasting or sent from the script editor), python will try to execute it, and when ready, will show the results with an `Out [..]:` prompt and come back with a new `In [..]:` prompt to wait for new commands. 

If python is still waiting for you to enter more data because it isn’t complete yet, the console will show a `...:` prompt. It means that you haven’t finished entering a complete command. This can be because you have not ‘closed’ a parenthesis or quotation, i.e. you don’t have the same number of left-parentheses as right-parentheses, or the same number of opening and closing quotation marks. When this happens, and you thought you finished typing your command, click inside the console window and press Esc; this will cancel the incomplete command and return you to the `In [..]:` prompt.

## How to learn more after the workshop?
The material we cover during this workshop will give you an initial taste of how you can use python to analyze data for your own research. However, you will need to learn more to do advanced operations such as cleaning your dataset, using statistical methods, or creating beautiful graphics. The best way to become proficient and efficient at python, as with any other tool, is to use it to address your actual research questions. As a beginner, it can feel daunting to have to write a script from scratch, and given that many people make their code available online, modifying existing code to suit your purpose might make it easier for you to get started.

## Seeking help

* check under _Help_ menu
* type `help()` in console
* [python documentation](https://www.python.org/doc/)
* type `?object` or `help(object)` to get information about an object

Finally, a generic Google or internet search “python task” will often either send you to the appropriate module documentation or a helpful forum where someone else has already asked your question.

I am stuck… I get an error message that I don’t understand
Start by googling the error message. However, this doesn’t always work very well because often, package developers rely on the error catching provided by python. You end up with general error messages that might not be very helpful to diagnose a problem (e.g. “subscript out of bounds”). If the message is very generic, you might also include the name of the function or package you’re using in your query.

However, you should check Stack Overflow. Search using the [python] tag. Most questions have already been answered, but the challenge is to use the right words in the search to find the answers: <http://stackoverflow.com/questions/tagged/python>

## Asking for help
The key to receiving help from someone is for them to rapidly grasp your problem. You should make it as easy as possible to pinpoint where the issue might be.

Try to use the correct words to describe your problem. For instance, a package is not the same thing as a library. Most people will understand what you meant, but others have really strong feelings about the difference in meaning. The key point is that it can make things confusing for people trying to help you. Be as precise as possible when describing your problem.

If possible, try to reduce what doesn’t work to a simple reproducible example. If you can reproduce the problem using a very small data frame instead of your 50,000 rows and 10,000 columns one, provide the small one with the description of your problem. When appropriate, try to generalize what you are doing so even people who are not in your field can understand the question. For instance instead of using a subset of your real dataset, create a small (3 columns, 5 rows) generic one.

### Where to ask for help?
* The person sitting next to you during the workshop. Don’t hesitate to talk to your neighbor during the workshop, compare your answers, and ask for help. You might also be interested in organizing regular meetings following the workshop to keep learning from each other.
* Your friendly colleagues: if you know someone with more experience than you, they might be able and willing to help you.
* [Stack Overflow](http://stackoverflow.com/questions/tagged/python): if your question hasn’t been answered before and is well crafted, chances are you will get an answer in less than 5 min. Remember to follow their guidelines on how to ask a good question.
* [python mailing lists](https://www.python.org/community/lists/])

## More resources
[PyPI - the Python Package Index](https://pypi.python.org/pypi)