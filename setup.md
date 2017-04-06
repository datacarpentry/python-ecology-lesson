---
layout: page
title: Setup Instructions for Learners
permalink: /setup/
---

# Python

[Python](http://python.org) is a popular language for
scientific computing, and great for general-purpose programming as
well.  Installing all of its scientific packages individually can be
a bit difficult, so we recommend an all-in-one installer.

For this workshop we use Python version 3.x.

## Required Python Packages for this workshop

* [Pandas](http://pandas.pydata.org/)
* [Jupyter notebook](http://jupyter.org/)
* [Numpy](http://www.numpy.org/)
* [Matplotlib](http://matplotlib.org/)

## Install the workshop packages

For installing these packages we will use Anaconda or Miniconda.
They both use [Conda](http://conda.pydata.org/docs/), the main difference is
that Anaconda comes with a lot of packages pre-installed.
With Miniconda you will need to install the required packages.

### Anaconda installation

Anaconda will install the workshop packages for you.

#### Download and install Anaconda

Download and install [Anaconda](https://www.continuum.io/downloads).
Remember to download and install the installer for Python 3.x

### Miniconda installation

Miniconda is a "light" version of Anaconda. If you install and use Miniconda
you will also need to install the workshop packages.

#### Download and install Miniconda

Download and install [Miniconda](http://conda.pydata.org/miniconda.html)
following the instructions. Remember to download and run the installer for
Python 3.x.

#### Check the installation of Miniconda

From the terminal, type:

```
conda list
```

#### Install the required workshop packages with conda

From the terminal, type:

```
conda install -y numpy pandas matplotlib jupyter
```

## Launch a Jupyter notebook

After installing either Anaconda or Miniconda and the workshop packages,
launch a Jupyter notebook by typing this command from the terminal:

```
jupyter notebook
```

The notebook should open automatically in your browser. If it does not or you
wish to use a different browser, open this link: <http://localhost:8888>.

---

## Overview of the Jupyter notebook (Optional)

![Example Jupyter Notebook](./fig/0_jupyter_notebook_example.jpg)  
*Screenshot of a [Jupyter Notebook on quantum mechanics](https://github.com/jrjohansson/qutip-lectures) by Robert Johansson*

### How the Jupyter notebook works

After typing the command `jupyter notebook`, the following happens:

* A Jupyter Notebook server is automatically created on your local machine.
* The Jupyter Notebook server opens the Jupyter notebook client, also known
  as the notebook user interface, in your default web browser.
* The Jupyter Notebook server runs locally on your machine only and does not
  use an internet connection.
* The Jupyter Notebook server sends messages to the notebook open in your
  browser.
* The Jupyter Notebook server does the work and calculations, and the web
  browser renders the notebook.
* When you can create a new notebook and type code into the browser, the web
  browser and the Jupyter notebook server communicate with each other.
* The web browser then displays the updated notebook to you.

This workflow has several advantages:

- You can easily type, edit, and copy and paste blocks of code.
- Tab completion allows you to easily access the names of things you are using
  and learn more about them.
- It allows you to annotate your code with links, different sized text,
  bullets, etc. to make information more accessible to you and your
  collaborators.
- It allows you to display figures next to the code that produces them
  to tell a complete story of the analysis.

### How the notebook is stored

* The notebook file is stored in a format called JSON and has the suffix
  `.ipynb`.
* Just like HTML for a webpage, what's saved in a notebook file looks
  different from what you see in your browser.
* But this format allows Jupyter to mix software (in several languages) with
  documentation and graphics, all in one file.

### Notebook modes: Control and Edit

The notebook has two modes of operation: Control and Edit. Control mode lets
you edit notebook level features; while, Edit mode lets you change the
contents of a notebook cell. Remember a notebook is made up of a number of
cells which can contain code, markdown, html, visualizations, and more.

* Open a new notebook from the dropdown menu in the top right corner of the file browser page.
* Each notebook contains one or more cells that contain code, text, or images.

> ## Code vs. Text
>
> We often use the term "code" to mean
> "the source code of software written in a language such as Python".
> A "code cell" in a Notebook is a cell that contains software;
> a "text cell" is one that contains ordinary prose written for human beings.
{: .callout}

*   If you press "esc" and "return" alternately,
    the outer border of your code cell will change from gray/blue to green.
    *   The difference in color is subtle.
*   These are the control (gray) and edit (green) modes of your notebook.
*   In control mode, pressing the "H" key will provide
    a list of all the shortcut keys.
*   Control mode alows you to edit notebook-level features, and edit mode changes the content of cells.
*   When in control mode (esc/gray),
    *   The "B" key will make a new cell below the currently selected cell.
    *   The "A" key will make one above.
    *   The "X" key will delete the current cell.
*   All actions can be done using the menus,
    but there are lots of keyboard shortcuts to speed things up.
*   If you remember the "esc" and "H" shortcut, you will be able to find out all the rest.

> ## Control Vs. Edit
>
> In the Jupyter notebook page are you currently in control or edit mode?  
> Switch between the modes.
> Use the shortcuts to generate a new cell
> Use the shortcuts to delete a cell
>
> > ## Solution
> >
> > Control mode has a grey boarder and Edit mode has a green border
> > Use "esc" and "Enter" to switch between modes
> > You need to be in control mode (Hit "esc" if your cell is green).  Type "B" or "A".
> > You need to be in control mode (Hit "esc" if your cell is green).  Type "X".
> >
> {: .solution}
{: .challenge}

## Use the keyboard and mouse to select and edit cells.

*   Pressing the "return" key turns the border green and engages edit mode,
    which allows you to type within the cell.
*   Because we want to be able to write many lines of code in a single cell,
    pressing the "return" key when in edit mode (green) moves the cursor to the next line in the cell just like in a text editor.
*   We need some other way to tell the Notebook we want to run what's in the cell.
*   Pressing the "shift" and the "enter" key together will execute the contents of the cell.
*   Notice that the "return" and "shift" keys on the
    right of the keyboard are right next to each other.

## The Notebook will turn Markdown into pretty-printed documentation.

*   Notebooks can also render [Markdown][markdown].
    *   A simple plain-text format for writing lists, links,
        and other things that might go into a web page.
    *   Equivalently, a subset of HTML that looks like what you'd send in an old-fashioned email.
*   Turn the current cell into a Markdown cell by entering
    the control mode (esc/gray) and press the "M" key.
*   `In [ ]:` will disappear to show it is no longer a code cell
    and you will be able to write in Markdown.
*   Turn the current cell into a Code cell
    by entering the control mode (esc/gray) and press the "Y" key.
