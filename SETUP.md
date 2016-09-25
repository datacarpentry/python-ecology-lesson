# Setup instructions for Data Carpentry Python Lesson with Ecological Data

## Python
[Python](http://python.org) is a popular language for
scientific computing, and great for general-purpose programming as
well.  Installing all of its scientific packages individually can be
a bit difficult, so we recommend an all-in-one installer.

For this lecture we use Python version 3.x

## Python Packages we will use

* [Pandas](http://pandas.pydata.org/)
* [Jupyter notebook](http://jupyter.org/)
* [Numpy](http://www.numpy.org/)
* [Matplotlib](http://matplotlib.org/)


## How to install this Packages
For installing these packages we will use Anaconda or Miniconda.
They both use [Conda](http://conda.pydata.org/docs/), the main difference is that Anaconda comes with a lot of packages installed by default.
With Miniconda you need to install the packages that you need.

### Using Anaconda
If you use Anaconda all the packages you need will be installed with Anaconda.

#### Download and install Anaconda
Download and install [Anaconda](https://www.continuum.io/downloads).
Remember to download and install the installer for Python 3.x

### Using Miniconda
Miniconda is a "light" version of Anaconda, after you installed Miniconda you need to install the additional packages.

#### Download and install Miniconda
Download and install [Minicoda](http://conda.pydata.org/miniconda.html) following the instructions.
Remember to download and install the installer for Python 3.x

#### Check the installation of Miniconda
From the terminal type:
```
conda list
```

#### Install the additional packages required with Miniconda
From the terminal type:
```
conda install -y numpy pandas matplotlib jupyter
```

## Launch a Jupyter notebook
After you installed Anaconda or Miniconda (plus the additional packages) to launch a jupyter notebook you need to type this command from the terminal:
```
jupyter notebook
```
You can then connect to: http://localhost:8888
