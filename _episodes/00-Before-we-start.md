---
title: Before we start
teaching: 30
exercises: 0
questions:
  - "What is Python?"
  - "Why should I learn Python?"
objectives:
  - "Describe the purpose of the editor, console, help, variable explorer and file explorer panes in Spyder."
  - "Organize files and directories for a set of analyses as a Python project, and understand the purpose of the working directory."
  - "Know where to find help."
  - "Demonstrate how to provide sufficient information for troubleshooting with the Python user community."
keypoints:
  - "Python is an open source and platform independent programming language"
  - "SciPy ecosystem for Python provides the tools necessary for scientific computing"
  - "Jupyter Notebook and the Spyder IDE are great tools to code in and interact with Python with its large community it is easy to find help in the internet"
---

<br />
## What is Python?
Python is a general purpose programming language that supports rapid development of data analytics applications.
The word "Python" is used to refer to both, the programming language and the tool that executes the scripts 
written in Python language.

Its main advantages are:

* Free
* Open-source
* Available on all major platforms (macOS, Linux, Windows)
* Supported by Python Software Foundation
* Supports multiple programming paradigms
* Has large community
* Rich ecosystem of third-party packages

*So, why do you need Python for data analysis?*

### Easy to learn
Python is easier to learn than other programming languages. This is important because lower barriers mean it is 
easier for new members of the community get up to speed and begin contributing back.

### Reproducibility
Reproducibility is the ability to obtain the same results using the same dataset(s) and analysis.

Data analysis written as a Python script can be repeated on any platform. 
Moreover, if you collect more data you can easily and quickly re-run your analysis on a larger dataset.

An increasing number of journals and funding agencies expect analyses to be reproducible,
so knowing Python will give you an edge with these requirements.

### Versatility
Python is a versatile language that integrates with many existing applications to enable something completely amazing.
For example, one can use Pythong to generate manuscripts, so that if you need to update your data, analysis procedure,
or change something else, you can quickly regenerate all the figures and your manuscript will be updated automatically.

Python can read text files, connect to databases, and many other data formats, on your computer or on the web.

### Interdisciplinary and extensible
Python provides a framework that allows one to combine approaches from different research disciplines
to best suit your analytical needs for your data.

### Python has a large and welcoming community
Thousands of people use Python daily. Many of them are willing to help you through mailing lists and websites, 
such as [Stack Overflow](https://stackoverflow.com) and
[Anaconda community portal](https://www.anaconda.com/community/).

### Free, open-source, and cross-platform
We know we have already said that but it is worth repeating. 

<br />
## Knowing your way around Anaconda
The [Anaconda](https://www.anaconda.com) distribution includes Python as well as its popular packages,
such as the IPython console, Jupyter Notebook, and Spyder IDE.
Have a quick look around the Anaconda Navigator. You can launch programs from the Navigator or use the command line.

The [Jupyter Notebook](https://jupyter.org) is an open-source web application that allows you to create 
and share documents that contain live code, equations, visualizations and narrative text.
[Spyder](https://spyder-ide.github.io) is a popular way to write Python scripts and also to interact with the Python software;
it is an **Integrated Development Enviroment**, also called IDE.

Anaconda also comes with a package manager called [conda](https://conda.io/docs/),
It makes it easy to install and update additional packages.

<br />
## Getting set up
It is good practice to keep a set of related data, analyses, and text self-contained in a single folder, called the working directory. All of the scripts within this folder can then use relative paths to files that indicate where inside the project a file is located (as opposed to absolute paths, which point to where a file is on a specific computer). Working this way makes it a lot easier to move your project around on your computer and share it with others without worrying about whether or not the underlying scripts will still work.


### Organizing your working directory
Using a consistent folder structure across your projects will help keep things organized, and will also make it easy to find/file things in the future. This can be especially helpful when you have multiple projects. In general, you may create directories (folders) for scripts, data, and documents.

**`data/`** Use this folder to store your raw data and intermediate datasets you may create for the need of a particular analysis. For the sake of transparency and provenance, you should always keep a copy of your raw data accessible and do as much of your data cleanup and preprocessing as possible programmatically (i.e., with scripts, rather than manually). Separating raw data from processed data is also a good idea. For example, you could have files `data/raw/tree_survey.plot1.txt` and `...plot2.txt` kept separate from a `data/processed/tree.survey.csv` file generated by the `scripts/01.preprocess.tree_survey.py` script.

**`documents/`** This would be a place to keep outlines, drafts, and other text.

**`scripts/`** This would be the location to keep your Python scripts for different analyses or plotting, and potentially a separate folder for your functions (more on that later).
You may want additional directories or subdirectories depending on your project needs, but these should form the backbone of your working directory. For this workshop, we will need a `data/` folder to store our raw data, and we will create later a `data_output/` folder when we learn how to export data as CSV files.


## Interacting with Python
The basis of programming is that we write down instructions for the computer to follow, and then we tell the computer to follow those instructions. We write, or code, instructions in Python because it is a common language that both the computer and we can understand. We call the instructions commands and we tell the computer to follow the instructions by executing (also called running) those commands.

##### If you are working with Jupyter notebook:
You can type Python code into a code cell and then execute the code by pressing <kbd>Shift</kbd>+<kbd>Return</kbd>. Any output will be printed directly under the input cell. You can recognise a code cell by the `In[ ]:` at the beginning of the cell and output is marked by `Out[ ]:`. Pressing the __+__ button in the menu bar will add a new cell. All your commands as well as any output will be saved with the notebook.

##### If you are working with Spyder:

You can either use the console or use script files (plain text files that contain your code). The console pane (in Spyder, the bottom right panel) is the place where commands written in the Python language can be typed and executed immediately by the computer. It is also where the results will be shown for commands that have been executed. You can type commands directly into the console and press <kbd>Return</kbd> to execute those commands, but they will be forgotten when you close the session. Spyder uses the [IPython](http://ipython.org) console by default.

Because we want our code and workflow to be reproducible, it is better to type the commands we want in the script editor, and save the script. This way, there is a complete record of what we did, and anyone (including our future selves!) can easily replicate the results on their computer.

Spyder allows you to execute commands directly from the script editor by using the run buttons on top or keyboard shortcuts. To run the entire script click _Run file_ or press <kbd>F5</kbd>, to run the current line click _Run selection or current line_ or press <kbd>F9</kbd>, other run buttons allow to run script cells or go into debug mode. When using <kbd>F9</kbd>, the command on the current line in the script (indicated by the cursor) or all of the commands in the currently selected text will be sent to the console and executed.

At some point in your analysis you may want to check the content of a variable or the structure of an object, without necessarily keeping a record of it in your script. You can type these commands and execute them directly in the console. Spyder provides the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd> and <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> shortcuts to allow you to jump between the script and the console panes.

If Python is ready to accept commands, the IPython console shows an `In [..]:` prompt with the current console line number in `[]`. If it receives a command (by typing, copy-pasting or sent from the script editor), Python will try to execute it, and when ready, will show the results with an `Out [..]:` prompt and come back with a new `In [..]:` prompt to wait for new commands.

If Python is still waiting for you to enter more data because it isn’t complete yet, the console will show a `...:` prompt. It means that you haven’t finished entering a complete command. This can be because you have not ‘closed’ a parenthesis or quotation, i.e. you don’t have the same number of left-parentheses as right-parentheses, or the same number of opening and closing quotation marks. When this happens, and you thought you finished typing your command, click inside the console window and press Esc; this will cancel the incomplete command and return you to the `In [..]:` prompt.

## How to learn more after the workshop?
The material we cover during this workshop will give you an initial taste of how you can use Python to analyze data for your own research. However, you will need to learn more to do advanced operations such as cleaning your dataset, using statistical methods, or creating beautiful graphics. The best way to become proficient and efficient at python, as with any other tool, is to use it to address your actual research questions. As a beginner, it can feel daunting to have to write a script from scratch, and given that many people make their code available online, modifying existing code to suit your purpose might make it easier for you to get started.

## Seeking help

* check under the _Help_ menu
* type `help()`
* type `?object` or `help(object)` to get information about an object
* [Python documentation](https://www.python.org/doc/)

Finally, a generic Google or internet search "Python task" will often either send you to the appropriate module documentation or a helpful forum where someone else has already asked your question.

I am stuck… I get an error message that I don’t understand
Start by googling the error message. However, this doesn’t always work very well because often, package developers rely on the error catching provided by python. You end up with general error messages that might not be very helpful to diagnose a problem (e.g. "subscript out of bounds"). If the message is very generic, you might also include the name of the function or package you’re using in your query.

However, you should check Stack Overflow. Search using the [python] tag. Most questions have already been answered, but the challenge is to use the right words in the search to find the answers: <http://stackoverflow.com/questions/tagged/python>

### Asking for help
The key to receiving help from someone is for them to rapidly grasp your problem. You should make it as easy as possible to pinpoint where the issue might be.

Try to use the correct words to describe your problem. For instance, a package is not the same thing as a library. Most people will understand what you meant, but others have really strong feelings about the difference in meaning. The key point is that it can make things confusing for people trying to help you. Be as precise as possible when describing your problem.

If possible, try to reduce what doesn’t work to a simple reproducible example. If you can reproduce the problem using a very small data frame instead of your 50,000 rows and 10,000 columns one, provide the small one with the description of your problem. When appropriate, try to generalize what you are doing so even people who are not in your field can understand the question. For instance instead of using a subset of your real dataset, create a small (3 columns, 5 rows) generic one.

### Where to ask for help?
* The person sitting next to you during the workshop. Don’t hesitate to talk to your neighbor during the workshop, compare your answers, and ask for help. You might also be interested in organizing regular meetings following the workshop to keep learning from each other.
* Your friendly colleagues: if you know someone with more experience than you, they might be able and willing to help you.
* [Stack Overflow](http://stackoverflow.com/questions/tagged/python): if your question hasn’t been answered before and is well crafted, chances are you will get an answer in less than 5 min. Remember to follow their guidelines on how to ask a good question.
* [Python mailing lists](https://www.python.org/community/lists/])

## More resources
[PyPI - the Python Package Index](https://pypi.python.org/pypi)

[The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)

[Dive into Python 3](http://getpython3.com/diveintopython3/)

{% include links.md %}
