---
title: Setup
---

::::::::::::::::::::::::::::::::::::::::::  prereq

## Data

Data for this lesson is from the
[Portal Project Teaching Database](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
Specifically, we use the following eight data files:

- [surveys.csv](https://ndownloader.figshare.com/files/10717177)
- [surveys2001.csv](data/yearly_files/surveys2001.csv)
- [surveys2002.csv](data/yearly_files/surveys2002.csv)
- [species.csv](https://ndownloader.figshare.com/files/3299483)
- [speciesSubset.csv](data/speciesSubset.csv)
- [plots.csv](https://ndownloader.figshare.com/files/3299474)
- [bouldercreek\_09\_2013.txt](data/bouldercreek_09_2013.txt)
- [portal\_mammals.sqlite](https://ndownloader.figshare.com/files/11188550)

Please download them (by clicking on the corresponding links) and move them to the same directory, or
[download all the files as a zip](data/portal-teachingdb-master.zip)
which will give you everything in a single compressed file. You'll need to unzip
this file after downloading it.


::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::  prereq

## Installing Python using Anaconda

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of the scientific packages we use in the lesson
individually can be a bit cumbersome, and therefore recommend the all-in-one
installer [Anaconda][anaconda].

Regardless of how you choose to install it, please make sure you install Python
version 3.x (e.g., 3.6 is fine).


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::: discussion

## Installing Anaconda

Select your operating system from the options below.

:::::::::::::::::::::::::::::::::

:::::::::::: solution

### Windows {#anaconda-windows}

1. Open [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) in your web browser.

2. Download the Anaconda Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using the recommended settings.
  Make sure that **Register Anaconda as my default Python 3.x** option is checked --
  it should be in the latest version of Anaconda.

4. Verify the installation:
  click Start, search and select `Anaconda Prompt` from the menu.
  A window should pop up where you can now type commands
  such as checking your Conda installation with:
  
  ```bash
  conda --help
  ```

#### Video Tutorial

<div class="yt-wrapper2">

<div class="yt-wrapper">

<iframe type="text/html" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" src="https://www.youtube-nocookie.com/embed/xxQ0mzZ8UvA?modestbranding=1&playsinline=1&iv_load_policy=3&rel=0" class="yt-frame" allowfullscreen></iframe>

</div>

</div>

::::::::::::

:::::::::::: solution

### MacOS {#anaconda-macos}

1. Visit [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) in your web browser.

2. Download the Anaconda Python 3 installer for macOS.
  These instructions assume that you use the graphical installer `.pkg` file.

3. Follow the Anaconda Python 3 installation instructions.
  Make sure that the install location is set to "Install only for me"
  so Anaconda will install its files locally, relative to your home directory.
  Installing the software for all users tends to create problems in the long run
  and should be avoided.

4. Verify the installation:
  click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal.
  A window should pop up where you can now type commands
  such as checking your conda installation with:
  
  ```bash
  conda --help
  ```

#### Video Tutorial

<div class="yt-wrapper2">

<div class="yt-wrapper">

<iframe type="text/html" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" src="https://www.youtube-nocookie.com/embed/TcSAln46u9U?modestbranding=1&playsinline=1&iv_load_policy=3&rel=0" class="yt-frame" allowfullscreen></iframe>

</div>

</div>

::::::::::::

:::::::::::: solution

### Linux {#anaconda-linux}

Note that the following installation steps require you to work from the terminal (shell).
If you run into any difficulties, please request help before the workshop begins.

1. Open [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) in your web browser.

2. Download the Anaconda Python 3 installer for Linux.

3. Install Anaconda using all of the defaults for installation.
  
  - Open a terminal window.
  - Navigate to the folder where you downloaded the installer.
  - Type `bash Anaconda3-` and press <kbd>Tab</kbd>.
    The name of the file you just downloaded should appear.
  - Press <kbd>Return</kbd>
  - Follow the text-only prompts.  When the license agreement appears (a colon
    will be present at the bottom of the screen) press <kbd>Spacebar</kbd> until you see the
    bottom of the text. Type `yes` and press <kbd>Return</kbd> to approve the license. Press
    <kbd>Return</kbd> again to approve the default location for the files. Type `yes` and
    press <kbd>Return</kbd> to prepend Anaconda to your `PATH` (this makes the Anaconda
    distribution your user's default Python).

4. Verify the installation:
  this depends a bit on your Linux distribution, but often you will have an Applications listing
  in which you can select a Terminal icon you can click. A window should pop up where you can now
  type commands such as checking your conda installation with:
  
  ```bash
  conda --help
  ```

::::::::::::

## Required Python Packages

The following are packages needed for this workshop:

- [Pandas](https://pandas.pydata.org/)
- [Jupyter notebook][jupyter]
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Plotnine](https://plotnine.readthedocs.io/en/stable/)

All packages apart from `plotnine` will have automatically been installed with Anaconda
and we can use Anaconda as a package manager to install the missing `plotnine` package:
You need to open up a *Terminal*, if you are using Mac OSX, or Linux (see instructions above),
or launch an *anaconda-promt*, if you are using Windows. In your terminal window type the following:

```bash
conda install -y -c conda-forge plotnine
```

This will then install the latest version of plotnine into your conda environment.

## Required packages: Miniconda

Miniconda is a lightweight version of Anaconda. If you install Miniconda instead of Anaconda,
you need to install required packages manually in the following way:

```bash
conda install -y numpy pandas matplotlib jupyter
conda install -c conda-forge plotnine
```

### *(Alternative)* Installing required packages with environment file

Download the
[environment.yml](../episodes/files/environment.yml)
file by right-clicking the link and selecting save as.
In the directory where you downloaded the environment.yml file run:

```bash
conda env create -f environment.yml
```

Activate the new environment with:

```bash
conda activate python-ecology-lesson
```

You can deactivate the environment with:

```bash
conda deactivate
```

## Launch a Jupyter notebook

After installing either Anaconda or Miniconda and the workshop packages,
launch a Jupyter notebook by typing this command from the terminal:

```bash
jupyter notebook
```

The notebook should open automatically in your browser. If it does not or you
wish to use a different browser, open this link: [http://localhost:8888](https://localhost:8888).

For a brief introduction to Jupyter Notebooks, please consult our
[Introduction to Jupyter Notebooks](jupyter_notebooks.md) page.

[python]: https://www.python.org/
[anaconda]: https://www.anaconda.com/
[jupyter]: https://jupyter.org/



