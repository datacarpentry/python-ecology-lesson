---
layout: lesson
root: .
title: Starting With Data
---

## Working With Pandas DataFrames in Python


### Learning Objectives
* Explain what a library is, and what libraries are used for.
* Load a Python/Pandas library.
* Read tabular data from a file into Python using Pandas using `read_csv`.
* Learn about the Pandas DataFrame object.
* Learn about data slicing and indexing.
* Perform mathematical operations on numeric data.
* Create simple plots of data.

## Lesson overview

For this lesson, we will be using a subset of the data from Ernst et al.
[Long-term monitoring and experimental manipulation of a Chihuahuan Desert
ecosystem near Portal, Arizona,
USA](http://www.esapubs.org/archive/ecol/E090/118/default.htm) called the
[Portal Project Teaching
Database](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).

In this lesson, we will

1. Read the data file
2. Calculate statistics from the data
3. Create some basic statistical graphs

We will create a file with a set of commands that will do all those things.
The advantage to creating a file is that we have a record of _exactly_ what we
did, we can run it over and over and it will always do the same thing.  This
is a huge advantage if corrections are made to the data and the analyses need
to be rerun and the plots regenerated, or if you will have many datasets all
with the same structure and to which the same procedures will be applied.  For
example, if you get daily measurements of air quality, temperature, humidity,
and those are used the same way every day.  This makes our methods easily
reproducible.  We can provide the code and the data to our colleagues and they
can replicate our work.

There are several data files that are part of the teaching database, but we
will only use the `survey.csv` file for this lesson.

[https://ndownloader.figshare.com/files/2292172](https://ndownloader.figshare.com/files/2292172)

Download that now and place it into your lesson folder.

The study area was divided into plots (not to be confused with the graphical
plots we will create later), and for each specimen, the species was identified
along with its sex, weight, and the length of its hind foot.

In the data file, each row holds information for a single animal

| Column           | Description                        |
|------------------|------------------------------------|
| record_id        |  Unique id for the observation     |
| month            |  Month of observation              |
| day              |  Day of observation                |
| year             |  Year of observation               |
| plot_id          |  ID of a particular plot           |
| species_id       |  Two-letter code                   |
| sex              |  Sex of animal ("M", "F")          |
| hindfoot_length  |  Length of the hindfoot in mm      |
| weight           |  Weight of the animal in grams     |

---


## About Libraries

As we emphasize, reusing code is a good thing.  There is a lot of code that has
been written and collected into _libraries_, which are then made available for
others to install and use.  The great variety of available libraries is one
of Python's strenths.  A library typically contains a set of functions, and to
access the functions, you load the library.  One analogy is that a library is
like a music CD, where each function is a track.  If you load the music from the
CD into your music player, you can play the functions from it.  Like the music
player, two functions may have the same name, so usually the function will be
referred to with the library name (or an assigned alias), a dot, and the function
name.  Adding the library name unquely identifies a function.

## The Pandas library

The [Python Data Analysis Library](http://pandas.pydata.org/), or Pandas,
provides data structures and functions that are commonly used in data analysis
(as you would expect from the name), it produces high quality graphs by using
another library [matplotlib](http://matplotlib.org/), and Pandas integrates well
with other libraries that use yet another library, [NumPy](http://www.numpy.org/),
which provides most of the basic mathematical functionality.  That is a _lot_
of reuseable code!

Python doesn't load libraries unless it is told to. We add an `import` statement
to our code in order to use a library and its functions, and we add the name of
the library after the `import`.  For example,

```python
import pandas
```

Since the library name is used as a prefix to function names, it is common to give a
library an alias (a nickname) to decrease what we have to type.  This is done by
adding `as <alias>` to the import statement.  It is very common on the internet
to see people use the `pd` alias for Pandas, an we would load it with that alias
like this.

```python
import pandas as pd
```
From then on, we can use, for example, `pd.read_csv` instead of `pandas.read_csv`.
Your carpal tunnels will thank you.


## Reading data using Pandas

If you recall from the shell lessons, we can use the `head` command to look at
the first few rows of our data file, which look like this.

```
record_id,month,day,year,plot_id,species_id,sex,hindfoot_length,weight
1,7,16,1977,2,NL,M,32,
2,7,16,1977,3,NL,M,33,
3,7,16,1977,2,DM,F,37,
4,7,16,1977,7,DM,M,36,
5,7,16,1977,3,DM,M,35,
6,7,16,1977,1,PF,M,14,
7,7,16,1977,2,PE,F,,
8,7,16,1977,1,DM,M,37,
9,7,16,1977,1,DM,F,34,
```

We need to first load the Pandas library using the `pd` alias we saw above,
and we will also load the `os` library, which comes with Python, as it provides
useful functions to query our operating system

```python
import pandas as pd
import os
```

See the [Python OS Library documentation](https://docs.python.org/3/library/os.html)
for more details.  This library provides, among other things, a function to say
which directory we are in and another function to change directories. If
you are working in IPython Notebook, be sure to start the notebook in the
workshop repository.

You can use the `os.getcwd()` function to find the current directory name, and
you can use the `os.listdir()`function to list the files in it, so

```python
os.listdir(os.getcwd())
```
will print the files in the current directory.  If you do not see `surveys.csv`,

```python
os.chdir("/the/correct/path/here")
```

will fix that.

To read data from a `.csv` file, we will use the Pandas function `read_csv()`.
Remember, we are being kind to our wrists, so the full name will use the alias.

```python
pd.read_csv("surveys.csv")
```

The result of that command is what's called a _DataFrame_, which is just printed
(in abbreviated form, thankfully!) because we aren't saying to do anything else.

A DataFrame is a two-dimensional data structure that can store data of mixed
types (including strings, integers, floating point values, factors, and more)
in columns. It is similar to a spreadsheet, an SQL table, or the `data.frame` in
R.

Here's an even more abbreviated version of what that command prints.

```
record_id  month  day  year  plot_id species_id sex  hindfoot_length  weight
0          1      7   16  1977        2         NL   M               32   NaN
1          2      7   16  1977        3         NL   M               33   NaN
...
35547      35548     12   31  2002        7     DO    M               36   51
35548      35549     12   31  2002        5     NaN  NaN             NaN  NaN

[35549 rows x 9 columns]
```

We can see that there were 33,549 rows parsed. Each row has 9 columns. It
looks like  the `read_csv` function in Pandas read our file properly (compare
the values from using the shell's `head` and `tail` commands on
`surveys.csv`).  However, we haven't saved any data to memory so we can work
with it.  We need to assign the DataFrame to a variable. Remember that a
variable is a name, such as `x` or `data`, assigned ot an object.  To create a
new object and assign a variable name to it using an equals sign.

Let's call the imported survey data `surveys_df`:

```python
surveys_df = pd.read_csv("surveys.csv")
```

Notice when you assign the imported DataFrame to a variable, Python does not
produce any output on the screen. We can print the value of the `surveys_df`
object by typing its name into the Python command prompt.

```python
surveys_df
```

which prints contents like above

## Manipulating Our Species Survey Data

Now we can start manipulating our data. First, let's check the data type of the
data stored in `surveys_df` using the `type` method. The `type` method and
`__class__` attribute tell us that `surveys_df` is `<class 'pandas.core.frame.DataFrame'>`.

```python
type(surveys_df)
# this does the same thing as the above!
surveys_df.__class__
```
We can also enter `surveys_df.dtypes` at our prompt to view the data type for each
column in our DataFrame. `int64` represents numeric integer values - `int64` cells
can not store decimals. `object` represents strings (letters and numbers). `float64`
represents numbers with decimals.

	surveys_df.dtypes

which returns:

```
record_id            int64
month                int64
day                  int64
year                 int64
plot_id              int64
species_id          object
sex                 object
hindfoot_length    float64
weight             float64
dtype: object
```

We'll talk a bit more about what the different formats mean in a different lesson.

### Useful Ways to View DataFrame objects in Python

There are multiple methods that can be used to summarize and access the data
stored in DataFrames. Let's try out a few. Note that we call the method by using
the object name `surveys_df.method`. So `surveys_df.columns` provides an index
of all of the column names in our DataFrame.

## Challenges

Try out the methods below to see what they return.

1. `surveys_df.columns`.
2. `surveys_df.head()`. Also, what does `surveys_df.head(15)` do?
3. `surveys_df.tail()`.
4. `surveys_df.shape`. Take note of the output of the shape method. What format does it return the shape of the DataFrame in?

HINT: [More on tuples, here](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences).


## Calculating Statistics From Data In A Pandas DataFrame

We've read our data into Python. Next, let's perform some quick summary
statistics to learn more about the data that we're working with. We might want
to know how many animals were collected in each plot, or how many of each
species were caught. We can perform summary stats quickly using groups. But
first we need to figure out what we want to group by.

Let's begin by exploring our data:

```python
# Look at the column names
surveys_df.columns.values
```

which **returns**:

```
array(['record_id', 'month', 'day', 'year', 'plot_id', 'species_id', 'sex',
       'hindfoot_length', 'weight'], dtype=object)
```

Let's get a list of all the species. The `pd.unique` function tells us all of
the unique values in the `species_id` column.

```python
pd.unique(surveys_df.species_id)
```

which **returns**:

```python
array(['NL', 'DM', 'PF', 'PE', 'DS', 'PP', 'SH', 'OT', 'DO', 'OX', 'SS',
       'OL', 'RM', nan, 'SA', 'PM', 'AH', 'DX', 'AB', 'CB', 'CM', 'CQ',
       'RF', 'PC', 'PG', 'PH', 'PU', 'CV', 'UR', 'UP', 'ZL', 'UL', 'CS',
       'SC', 'BA', 'SF', 'RO', 'AS', 'SO', 'PI', 'ST', 'CU', 'SU', 'RX',
       'PB', 'PL', 'PX', 'CT', 'US'], dtype=object)
```

## Challenges

1. Create a list of unique plot ID's found in the surveys data. Call it
   `plotNames`. How many unique plots are there in the data? How many unique
   species are in the data?

# Groups in Pandas

We often want to calculate summary statistics grouped by subsets or attributes
within fields of our data. For example, we might want to calculate the average
weight of all individuals per plot.

We can calculate basic statistics for all records in a single column using the
syntax below:

```python
surveys_df['weight'].describe()
```
gives **output**

```python
count    32283.000000
mean        42.672428
std         36.631259
min          4.000000
25%         20.000000
50%         37.000000
75%         48.000000
max        280.000000
Name: weight, dtype: float64
```

We can also extract one specific metric if we wish:

```python
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()
```

But if we want to summarize by one or more variables, for example sex, we can
use Pandas' `.groupby` method. Once we've created a groupby DataFrame, we
can quickly calculate summary statistics by a group of our choice.

```python
# Group data by sex
sorted = surveys_df.groupby('sex')
```

The Pandas function `describe` will return descriptive stats including: mean,
median, max, min, std and count for a particular column in the data. Pandas'
`describe` function will only return summary values for columns containing
numeric data.

```python
# summary statistics for all numeric columns by sex
sorted.describe()
# provide the mean for each numeric column by sex
sorted.mean()
```

`sorted.mean()` **OUTPUT:**

```python
        record_id     month        day         year    plot_id  \
sex                                                              
F    18036.412046  6.583047  16.007138  1990.644997  11.440854   
M    17754.835601  6.392668  16.184286  1990.480401  11.098282   

     hindfoot_length     weight  
sex                              
F          28.836780  42.170555  
M          29.709578  42.995379  

```

The `groupby` command is powerful in that it allows us to quickly generate
summary stats.

# Challenge

1. How many recorded individuals are female `F` and how many male `M`
2. What happens when you group by two columns using the following syntax and
    then grab mean values:
	- `sorted2 = surveys_df.groupby(['plot_id','sex'])`
	- `sorted2.mean()`
3. Summarize weight values for each plot in your data. HINT: you can use the
   following syntax to only create summary statistics for one column in your data
   `byPlot['weight'].describe()`


Did you get #3 right? **A Snippet of the Output from challenge 3 looks like:**

```
	plot
	1     count    1903.000000
	      mean       51.822911
	      std        38.176670
	      min         4.000000
	      25%        30.000000
	      50%        44.000000
	      75%        53.000000
	      max       231.000000
          ...
```

## Quickly Creating Summary Counts in Pandas

Let's next create a list of unique species in our data. We can do this in a few
ways, but we'll use `groupby` combined with a `count()` method.


```python
# count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
```

Or, we can also count just the rows that have the species "DO":

```python
surveys_df.groupby('species_id')['record_id'].count()['DO']
```

## Basic Math Functions

If we wanted to, we could perform math on an entire column of our data. For
example let's multiply all weight values by 2. A more practical use of this might
be to normalize the data according to a mean, area, or some other value
calculated from our data.

	# multiply all weight values by 2
	surveys_df['weight']*2


## Another Challenge

1. What's another way to create a list of species and associated `count` of the
   records in the data? Hint: you can perform `count`, `min`, etc functions on
   groupby DataFrames in the same way you can perform them on regular
   DataFrames.


# Quick & Easy Plotting Data Using Pandas

We can plot our summary stats using Pandas, too.

	# make sure figures appear inline in Ipython Notebook
	%matplotlib inline
	# create a quick bar chart
	species_counts.plot(kind='bar');

![Weight by Species Plot](img/weightBySpecies.png)
Weight by species plot

We can also look at how many animals were captured in each plot:

```python
total_count=surveys_df.record_id.groupby(surveys_df['plot_id']).nunique()
# let's plot that too
total_count.plot(kind='bar');
```

# Challenge Activities

1. Create a plot of average weight across all species per plot.
2. Create a plot of total males versus total females for the entire dataset.


# Summary Plotting Challenge

Create a stacked bar plot, with weight on the Y axis, and the stacked variable
being sex. The plot should show total weight by sex for each plot. Some
tips are below to help you solve this challenge:

* [For more on Pandas plots, visit this link.](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.core.groupby.DataFrameGroupBy.plot.html)
* You can use the code that follows to create a stacked bar plot but the data to stack
  need to be in individual columns.  Here's a simple example with some data where
  'a', 'b', and 'c' are the groups, and 'one' and 'two' are the subgroups.

```
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
pd.DataFrame(d)
```

shows the following data

```
       one  two
   a    1    1
   b    2    2
   c    3    3
   d  NaN    4
```

We can plot the above with

```
# plot stacked data so columns 'one' and 'two' are stacked
my_df = pd.DataFrame(d)
my_df.plot(kind='bar',stacked=True,title="The title of my graph")
```

![Stacked Bar Plot](img/stackedBar1.png)

* You can use the `.unstack()` method to transform grouped data into columns
for each plotting.  Try running `.unstack()` on some DataFrames above and see
what it yields.

Start by transforming the grouped data (by plot and sex) into an unstacked layout, then create
a stacked plot.


## Solution to Summary Challenge

First we group data by plot and by sex, and then calculate a total for each plot.

```python
by_plot_sex = surveys_df.groupby(['plot_id','sex'])
plot_sex_count = by_plot_sex['weight'].sum()
```

This calculates the sums of weights for each sex within each plot as a table

```
plot  sex
plot_id  sex
1        F      38253
         M      59979
2        F      50144
         M      57250
3        F      27251
         M      28253
4        F      39796
         M      49377
<other plots removed for brevity>
```

Below we'll use `.unstack()` on our grouped data to figure out the total weight that each sex contributed to each plot.

```python
by_plot_sex = surveys_df.groupby(['plot_id','sex'])
plot_sex_count = by_plot_sex['weight'].sum()
plot_sex_count.unstack()
```

The `unstack` function above will display the following output:

```
sex          F      M
plot_id              
1        38253  59979
2        50144  57250
3        27251  28253
4        39796  49377
<other plots removed for brevity>
```

Now, create a stacked bar plot with that data where the weights for each sex are stacked by plot.

Rather than display it as a table, we can plot the above data by stacking the values of each sex as follows:

```python
by_plot_sex = surveys_df.groupby(['plot_id','sex'])
plot_sex_count = by_plot_sex['weight'].sum()
spc = plot_sex_count.unstack()
s_plot = spc.plot(kind='bar',stacked=True,title="Total weight by plot and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Plot")
```

![Stacked Bar Plot](img/stackedBar.png)
