---
layout: page
title: Setup
---

> ## Data
> Data for this lesson is from the
> [Portal Project Teaching Database](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
> Specifically, we use the following eight data files:
> - [surveys.csv](https://ndownloader.figshare.com/files/10717177)
> - [surveys2001.csv]({{ page.root }}/data/yearly_files/surveys2001.csv)
> - [surveys2002.csv]({{ page.root }}/data/yearly_files/surveys2002.csv)
> - [species.csv](https://ndownloader.figshare.com/files/3299483)
> - [speciesSubset.csv]({{ page.root }}/data/speciesSubset.csv)
> - [plots.csv](https://ndownloader.figshare.com/files/3299474)
> - [bouldercreek_09_2013.txt]({{ page.root }}/data/bouldercreek_09_2013.txt)
> - [portal_mammals.sqlite](https://ndownloader.figshare.com/files/11188550)
>
> Please download them (by clicking on the corresponding links) and move them to the same directory, or
> [download all the files as a zip]({{ page.root }}/data/portal-teachingdb-master.zip)
> which will give you everything in a single compressed file. You'll need to unzip
> this file after downloading it.
{: .prereq}



> ## Installing Python using Anaconda
> [Python][python] is a popular language for scientific computing, and great for
> general-purpose programming as well. Installing all of its scientific packages
> individually can be a bit difficult, however, so we recommend the all-in-one
> installer [Anaconda][anaconda].
>
> Regardless of how you choose to install it, please make sure you install Python
> version 3.x (e.g., 3.6 is fine). Also, please set up your Python environment at 
> least a day in advance of the workshop.  If you encounter problems with the 
> installation procedure, ask your workshop organizers via e-mail for assistance so
> you are ready to go as soon as the workshop begins.
{: .prereq}

### Windows - [Video tutorial][video-windows]

1. Open <https://www.anaconda.com/products/individual> in your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using the recommended settings. Make sure that **Register Anaconda as my default Python 3.x** option is checked - it should be in the latest version of Anaconda


### Mac OS X - [Video tutorial][video-mac]

1. Visit <https://www.anaconda.com/products/individual> in your web browser.

2. Download the Python 3 installer for OS X. These instructions assume that you use the graphical installer `.pkg` file.

3. Follow the Python 3 installation instructions. Make sure that the install location is set to "Install only for me" so Anaconda will install its files locally, relative to your home directory. Installing the software for all users tends to create problems in the long run and should be avoided.


### Linux

Note that the following installation steps require you to work from the terminal (shell). 
If you run into any difficulties, please request help before the workshop begins.

1.  Open [https://www.anaconda.com/distribution/][anaconda-linux] with your web browser.

2.  Download the Python 3 installer for Linux.

3.  Install Python 3 using all of the defaults for installation.

    a.  Open a terminal window.

    b.  Navigate to the folder where you downloaded the installer

    c.  Type

    ~~~
    $ bash Anaconda3-
    ~~~
    {: .bash}

    and press tab.  The name of the file you just downloaded should appear.

    d.  Press enter.

    e.  Follow the text-only prompts.  When the license agreement appears (a colon
        will be present at the bottom of the screen) press the space bar until you see the 
        bottom of the text. Type `yes` and press enter to approve the license. Press 
        enter again to approve the default location for the files. Type `yes` and 
        press enter to prepend Anaconda to your `PATH` (this makes the Anaconda 
        distribution your user's default Python).


[anaconda]: https://www.anaconda.com/
[jupyter]: https://jupyter.org/
[python]: https://www.python.org/
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA

## Opening a Conda-enabled Terminal and Verifying the Installation:

### Windows
Click Start, search, or select Anaconda Prompt from the menu. A window should pop up where you can now type commands such as checking your Conda installation with:

~~~
conda --help
~~~
{: .language-bash}

### Mac OSX

Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal. 
A window should pop up where you can now type commands such as checking your conda installation with:

~~~
conda --help
~~~
{: .language-bash}

### Linux
This depends a bit on your Linux distribution, but often you will have an Applications listing in which you can select a Terminal icon you can click. A window should pop up where you can now type commands such as checking your conda installation with:

~~~
conda --help
~~~
{: .language-bash}


## Required Python Packages for this Workshop
The following are packages needed for this workshop:

* [Pandas](http://pandas.pydata.org/)
* [Jupyter notebook](http://jupyter.org/)
* [Numpy](http://www.numpy.org/)
* [Matplotlib](http://matplotlib.org/)
* [Plotnine](https://plotnine.readthedocs.io/en/stable/)

All packages apart from plotnine will have automatically been installed with Anaconda and we can use anaconda as a package manager to install the missing `plotnine` package:
You need to open up a *Terminal*, if you are using Mac OSX, or Linux (see instructions above), or launch an *anaconda-promt*, if you are using Windows. In your terminal window type the following: 

~~~
conda install -y -c conda-forge plotnine
~~~
{: .language-bash}

This will then install the latest version of plotnine into your conda environment. 

## Installing other Packages (Not required)
If you want to install any additional packages, you can do so by opening a terminal window and type:
~~~
conda install -y package_name
~~~
{: .language-bash}

You may need to install the required packages in this way, if you opted for installing Miniconda, instead of Anaconda. Miniconda is a "light" version of Anaconda. If you install and use Miniconda
you will also need to install the workshop packages manually in the following way:
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
