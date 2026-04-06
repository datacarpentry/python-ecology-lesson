---
title: Instructor Notes
---

## Install the required workshop packages

Please use the instructions in the [Setup][lesson-setup] document to perform installs. If you
encounter setup issues, please file an issue with the tags 'High-priority'.

## Checking installations.

In the [`episodes/files/scripts/check_env.py`](../episodes/files/scripts/check_env.py) directory, you will find a script called check\_env.py This checks the
functionality of the Anaconda install.

By default, Data Carpentry does not have people pull the whole repository with all the scripts and
addenda. Therefore, you, as the instructor, get to decide how you'd like to provide this script to
learners, if at all.  To use this, students can navigate into `_includes/scripts` in the terminal, and
execute the following:

```bash
python check_env.py
```

If learners receive an `AssertionError`, it will inform you how to help them correct this
installation. Otherwise, it will tell you that the system is good to go and ready for Data
Carpentry!

## 07-visualization-ggplot-python

iPython notebooks for plotting can be viewed in the `learners` folder.

## 08-putting-it-all-together

Answers are embedded with challenges in this lesson, 
other than random distribtuion which is left to the learner to choose,
and final plot, for which the learner should investigate the matplotlib gallery.

Scientists often operate on mathematical equations.
Being able to use them in their graphics has a lot of added value
Luckily, Matplotlib provides powerful tools for text control.
One of them is the ability to use LaTeX mathematical notation, 
whenever text is used
(you can learn more about LaTeX math notation here: [https://en.wikibooks.org/wiki/LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)).
To use mathematical notation, surround your text using the dollar sign ("$").

LaTeX uses the backslash character ("\\") a lot.
Since backslash has a special meaning in the Python strings,
you should replace all the LaTeX-related backslashes with two backslashes.

```python
plt.plot(t, t, 'r--', label='$y=x$')
plt.plot(t, t**2 , 'bs-', label='$y=x^2$')
plt.plot(t, (t - 5)**2 + 5 * t - 0.5, 'g^:', label='$y=(x - 5)^2 + 5  x - \\frac{1}{2}$') # note the double backslash

plt.legend(loc='upper left', shadow=True, fontsize='x-large')

# Note the double backslashes in the line below.
plt.xlabel('This is the x axis. It can also contain math such as $\\bar{x}=\\frac{\\sum_{i=1}^{n} {x}} {N}$')
plt.ylabel('This is the y axis')
plt.title('This is the figure title')

plt.show()
```

[This page][matplotlib-mathtext] contains more information.

[matplotlib-mathtext]: https://matplotlib.org/users/mathtext.html



