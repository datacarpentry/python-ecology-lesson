---
layout: page
title: Setup
---

> ## Data
> Data for this lesson are from the Portal Project Teaching Database -
> [available on FigShare](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
>
> We will use the six files listed below for the data in this lesson.
> Download these files to your computer by clicking
> [this link](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/weecology/portal-teachingdb),
> which will give you everything in a single compressed file.
> You'll need to unzip this file after downloading it.
>
> Or download each file indvidually with the following links:
>
> - [surveys.csv](https://ndownloader.figshare.com/files/10717177)
> - [species.csv](https://ndownloader.figshare.com/files/3299483)
> - [speciesSubset.csv]({{ page.root }}/data/speciesSubset.csv)
> - [plots.csv](https://ndownloader.figshare.com/files/3299474)
> - [bouldercreek_09_2013.txt]({{ page.root }}/data/bouldercreek_09_2013.txt)
> - [SQL Database](https://ndownloader.figshare.com/files/11188550)
{: .prereq}



> ## Software
> [Python](http://python.org) is a popular language for
> scientific computing and is great for general-purpose programming as
> well.  Installing all of its scientific packages individually can be
> a bit difficult, so we recommend an all-in-one installer.
>
> For this workshop we use Python version 3.x.
>
> ### Required Python packages for this workshop
>
> * [Pandas](http://pandas.pydata.org/)
> * [Jupyter Notebook](http://jupyter.org/)
> * [Numpy](http://www.numpy.org/)
> * [Matplotlib](http://matplotlib.org/)
> * [plotnine](https://github.com/has2k1/plotnine)
{: .prereq}

## Software installation

We will use either Anaconda or Miniconda to install Python and the required packages.
They both use [Conda](http://conda.pydata.org/docs/), but
Anaconda comes with Pandas, Jupyter, Numpy and Matplotlib pre-installed while
Miniconda does not.

### Anaconda installation

Anaconda will install the workshop packages for you.

#### Download and install Anaconda

Download and install [Anaconda](https://www.continuum.io/downloads).
Remember to download and install the installer for Python 3.x.

#### Download the plotting package

The plotting package `plotnine` is not installed by default.  
To install it from the terminal, type:

~~~
conda install -c conda-forge plotnine
~~~
{: .language-python}

### Miniconda installation

Miniconda is a "lightweight" version of Anaconda. 
If you install and use Miniconda,
you will also need to install the workshop packages.

#### Download and install Miniconda

Download and install [Miniconda](http://conda.pydata.org/miniconda.html)
following the instructions. Remember to download and run the installer for
Python 3.x.

#### Check the installation of Miniconda

In the terminal, type:

~~~
conda list
~~~
{: .language-bash}

### Install the required workshop packages with Conda

In the terminal, type:

~~~
conda install -y numpy pandas matplotlib jupyter
conda install -c conda-forge plotnine
~~~
{: .language-bash}

## Launch a Jupyter Notebook

After installing Python and the required packages,
launch a Jupyter Notebook by typing this command in the terminal:

~~~
jupyter notebook
~~~
{: .language-bash}

A Jupyter Notebook notebook should open automatically in your browser. If it does not, or you
wish to use a different browser, open this link: <http://localhost:8888>.

For a brief introduction to Jupyter Notebooks, please consult with our
[Introduction to Jupyter Notebooks](jupyter_notebooks) page.
