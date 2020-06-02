---
layout: page
title: Setup
---

> ## Data
<<<<<<< Updated upstream
> Data for this lesson is based on the Portal Project Teaching Database -
> [available on FigShare](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
>
> For this lesson we will use the eight files listed below for data.
> These can be download by following the below links
=======
> Data for this lesson is from the Portal Project Teaching Database
> [which can be found on FigShare](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
> Specifically, we use the following eight data files:
>>>>>>> Stashed changes
>
> - [surveys.csv](https://ndownloader.figshare.com/files/10717177)
> - [surveys2001.csv]({{ page.root }}/data/surveys2001.csv)
> - [surveys2002.csv]({{ page.root }}/data/surveys2002.csv)
> - [species.csv](https://ndownloader.figshare.com/files/3299483)
> - [speciesSubset.csv]({{ page.root }}/data/speciesSubset.csv)
> - [surveys2001.csv]({{ page.root }}/data/yearly_files/surveys2001.csv)
> - [surveys2002.csv]({{ page.root }}/data/yearly_files/surveys2002.csv)
> - [plots.csv](https://ndownloader.figshare.com/files/3299474)
> - [bouldercreek_09_2013.txt]({{ page.root }}/data/bouldercreek_09_2013.txt)
<<<<<<< Updated upstream
> - [SQL Database](https://ndownloader.figshare.com/files/11188550)

> Five of the above eight files can also be obtained via
> [this link](https://github.com/weecology/portal-teachingdb/archive/master.zip),
> returning a single compressed file.
> You'll need to unzip this file after downloading it, but also manually download the remaining three files
> [surveys2001.csv]({{ page.root }}/data/yearly_files/surveys2001.csv),
> [surveys2002.csv]({{ page.root }}/data/yearly_files/surveys2002.csv) and
> [bouldercreek_09_2013.txt]({{ page.root }}/data/bouldercreek_09_2013.txt).
=======
> - [portal_mammals.sqlite](https://ndownloader.figshare.com/files/11188550)
>
> Please download them (by clicking on the corresponding links) and move them to the same directory, or
> [download all the files as a zip]({{ page.root }}/data/portal-teachingdb-master.zip)
> which will give you everything in a single compressed file. You'll need to unzip
> this file after downloading it.
>>>>>>> Stashed changes
{: .prereq}



> ## Software
> [Python](http://python.org) is a popular language for
> scientific computing, and great for general-purpose programming as
> well.  Installing all of its scientific packages individually can be
> a bit difficult, so we recommend an all-in-one installer.
>
> For this workshop we use Python version 3.x.
>
> ### Required Python Packages for this workshop
>
> * [Pandas](http://pandas.pydata.org/)
> * [Jupyter notebook](http://jupyter.org/)
> * [Numpy](http://www.numpy.org/)
> * [Matplotlib](http://matplotlib.org/)
{: .prereq}

## Install the workshop packages

For installing these packages we will use Anaconda or Miniconda.
They both use [Conda](https://conda.io/en/latest/), the main difference is
that Anaconda comes with a lot of packages pre-installed.
With Miniconda you will need to install the required packages.

### Anaconda installation

Anaconda will install the workshop packages for you.

#### Download and install Anaconda

Download and install [Anaconda](https://www.anaconda.com/distribution/#download-section).
Remember to download and install the installer for Python 3.x.

#### Download plotting package

The plotting package plotnine is not installed by default.  From the terminal,
type:

~~~
conda install -c conda-forge plotnine
~~~
{: .language-bash}

### Miniconda installation

Miniconda is a "light" version of Anaconda. If you install and use Miniconda
you will also need to install the workshop packages.

#### Download and install Miniconda

Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
following the instructions. Remember to download and run the installer for
Python 3.x.

#### Check the installation of Miniconda

From the terminal, type:

~~~
conda list
~~~
{: .language-bash}

### Install the required workshop packages with conda

From the terminal, type:

~~~
conda install -y numpy pandas matplotlib jupyter
conda install -c conda-forge plotnine
~~~
{: .language-bash}

## Launch a Jupyter notebook

After installing either Anaconda or Miniconda and the workshop packages,
launch a Jupyter notebook by typing this command from the terminal:

~~~
jupyter notebook
~~~
{: .language-bash}

The notebook should open automatically in your browser. If it does not or you
wish to use a different browser, open this link: <http://localhost:8888>.

For a brief introduction to Jupyter Notebooks, please consult our
[Introduction to Jupyter Notebooks](jupyter_notebooks) page.
