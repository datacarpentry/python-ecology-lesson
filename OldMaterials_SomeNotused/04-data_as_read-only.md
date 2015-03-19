##Treating your data as read-only

In today's scientific climate, there is more attention being paid to reproducibilty and data availability. Upon publication, you may be asked to provide both raw and processed data. Likewise, funding agencies may require that your data is made open-access or deposited in public repositories. In the absence of external pressure, you still likely want to have your raw data around, in case you decide to reanalyze it or use it for meta-analysis in the future. This tutorial is intended to offer you a short look at the os module, and how you can leverage it to help you keep your raw and processed data separated.

##os module

The os module is included in the base Python library and can be loaded in the standard way:

```python
import os
```

This library offers assorted functions for interacting with the operating system. In this lesson, we'll be looking at creating and populating directories from within a script.

##Data as read-only

Data as read-only means exactly that: when you interact with a file, you don't make changes to that file. Instead, you make your edits programmatically and save the edited files to a separate location. Let's grab our survey data:

```python
import pandas as pd
mydata = pd.read_csv("data/surveys.csv")
```

As a refresher, here is a function from lesson 3 that fills in missing data with zeros:

```python
mydata['wgt'] = mydata['wgt'].fillna(0)
```

We've already learned how to write this to a file. And for many purposes, writing to a file might be sufficient. But other people don't know our data as well as we do. Delineating between raw and processed files can be very helpful when others need to interact with our data.

We're going to start out by checking to see if we have a directory for our processed data.

```python

if 'processed' in os.listdir('.'):
    print 'yay'
else:
    print 'nay'
```

What we've done above is used the os module to list all the directories in our current directory, denoted as '.' (If this syntax is unfamiliar, have a look through our shell [materials](https://github.com/datacarpentry/datacarpentry/blob/master/lessons/shell/01-filedir.md)). If our current directory contains a directory called 'processed', we celebrate in a restrained and dignified way. If not, we don't. 

Just printing things isn't that useful. Let's try something else:

```python
if 'processed' in os.listdir('.'):
    print 'Processed directory exists'
else:
    os.mkdir('processed')
    print 'Processed directory created'   
```

Now, what our code does is creates a directory and informs us of this fact.

We can combine this with what we've learned about writing output from Pandas to treat our data as read-only:

```python


mydata.to_csv('processed/surveys.csv')

```

##Wrap-Up

What we've covered in this lesson is:

* What it means to treat data as read-only.
* Why we might want to treat our data as read-only.
* How we can use the os module to keep our processed and raw data straight.


