# Analyzing Survey Data

We are studying the species and weight of animals caught in plots in our study area.
The data sets are stored in .csv each row holds information for a single animal,
and the columns represent record_id,month,day,year,plot,species,sex,wgt
The first few rows of our first file look like this:

"63","8","19","1977","3","DM","M","40"

"64","8","19","1977","7","DM","M","48"

"65","8","19","1977","4","DM","F","29"

"66","8","19","1977","4","DM","F","46"

"67","8","19","1977","7","DM","M","36"

### We want to:

* load that data into memory,
* calculate the average weight of the animals across all animals, and
* plot the result.
To do all that, we'll have to learn a little bit about programming.

### Objectives
* Explain what a library is, and what libraries are used for.
* Load a Python/pandas library and use the things it contains.
* Read tabular data from a file into a program.
* Assign values to variables.
* Learn about data types
* Select individual values and subsections from data.
* Perform operations on arrays of data.
* Display simple graphs.

## Loading Data
----------------

Words are useful, but what's more useful are the sentences and stories we use them to build.
Similarly, while a lot of powerful tools are built into languages like Python,
even more lives in the libraries they are used to build.
Importing a library is like getting a piece of lab equipment out of a storage locker
and setting it up on the bench.
Once it's done, we can ask the library to do things for us.

If someone want to use python for data analysis the best solution is to use [Python Data Analysis Library](http://pandas.pydata.org/) (a.k.a. pandas). It provides data structures, produces high quality plots with [matplotlib](http://matplotlib.org/), and integrates nicely with other libraries that expect [NumPy](http://www.numpy.org/) arrays.

### Installing pandas

If you use pip installing pandas should be easy:

```
[user@host:python]$sudo pip install pandas
```

For more complex scenarios, please see the [installation instructions](http://pandas.pydata.org/pandas-docs/stable/install.html).

To start working with pandas user should open ipython shell in folder with python lessons

```
[user@host:python]$ipython
```

then import pandas library into python shell

```python
import pandas
```

Secondly, let's locate and read our data. Because it is in a CSV file, we can use pandas' `read_csv` function to pull it directly into a [DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe).

### Variables

```python
pandas.read_csv("data/surveys.csv")
```

which gives **output**:

```
       record_id  month  day  year  plot species  sex  wgt
0              1      7   16  1977     2     NaN    M  NaN
1              2      7   16  1977     3     NaN    M  NaN
2              3      7   16  1977     2      DM    F  NaN
3              4      7   16  1977     7      DM    M  NaN
4              5      7   16  1977     3      DM    M  NaN
5              6      7   16  1977     1      PF    M  NaN
6              7      7   16  1977     2      PE    F  NaN
7              8      7   16  1977     1      DM    M  NaN
8              9      7   16  1977     1      DM    F  NaN
9             10      7   16  1977     6      PF    F  NaN
10            11      7   16  1977     5      DS    F  NaN
11            12      7   16  1977     7      DM    M  NaN
12            13      7   16  1977     3      DM    M  NaN
13            14      7   16  1977     8      DM  NaN  NaN
...
[35549 rows x 8 columns]
```

We could see, that there were 33549 rows parsed, each of them consisting 8 columns. Our call to `pandas.read_csv` read our file, but it haven't saved any data in memory. If we want that, we need to assign the data frame to a variable. A variable is just a name for a value, such as x, current_temperature, or subject_id. We can create a new variable simply by assigning a value to it using `=`. For example,

```python
weight_kg = 55
```

When we gave variable a value, we can print it:

```python
weight_kg
```

which gives **output**

```
55
```

and manipulate whit it, for example multiply it:

```python
3.5*weight_kg
```

which gives **output**

```
192.5
```

We can also change a variable's value by assigning it a new one and print out the information using 'print' to add text and values together:

```python
weight_kg = 52
print "person lost some weight and now weights", weight_kg
```

which gives **output**

```
person lost some weight and now weights  52
```

If we imagine the variable as a sticky note with a name written on it, assignment is like putting the sticky note on a particular value. This means that assigning a value to one variable does not change the values of other variables. For example, let's store the animal's weight in pounds in a variable:

```python
weight_lb = 2.2 * weight_kg
print "animal's weight in kilograms:", weight_kg, "and in pounds:", weight_lb
```

which gives **output**

```
animal's weight in kilograms: 52 and in pounds: 114.4
```

and then change variable weight_kg

```python
weight_kg = 80
print "animal weight in kilograms:", weight_kg, "but in pounds is still", weight_lb
```

which gives **output**

```
animal's weight in kilograms: 80 but in pounds is still 114.4
```

#### Updating a Variable

Since variable `weight_lb` doesn't "remember" where its value came from, it isn't automatically updated when variable `weight_kg` changes. This is different from the way spreadsheets work.

#### Challenges

Draw diagrams showing what variables refer to what values after each statement in the following commands:

```python
mass = 47.5
age  = 122
mass = mass * 2.0
age  = age - 20
```

**What is your answer?**


Variables also could be vectors or matricies.

```python
vector = [0,2.5]
matrix = [[0,2],[0,1]]
print "vector =", vector, "matrix =", matrix
```

which gives **output**

```
[0, 2.5] [[0, 2], [0, 1]]
```



Therefore, we can also add to variable that are vectors, and update them by making them longer. 
For example, if we are creating a vector of animal weights, we could update that vector using its iternal `.append` method. 

```print
weights = [100]
print weights
weights.append(80)
print weights
```

which gives **output**

```
[100]
[100, 80]
```

Now we can save data readed from csv file into variable:

```python
dat = pandas.read_csv("data/surveys.csv")
```

This statement will not produce any output, becouse assignment doesn't display anything. If we want to print loaded data we can use just

```python
dat
```

which gives **output**


```
       record_id  month  day  year  plot species  sex  wgt
0              1      7   16  1977     2     NaN    M  NaN
1              2      7   16  1977     3     NaN    M  NaN
2              3      7   16  1977     2      DM    F  NaN
3              4      7   16  1977     7      DM    M  NaN
4              5      7   16  1977     3      DM    M  NaN
5              6      7   16  1977     1      PF    M  NaN
6              7      7   16  1977     2      PE    F  NaN
7              8      7   16  1977     1      DM    M  NaN
8              9      7   16  1977     1      DM    F  NaN
9             10      7   16  1977     6      PF    F  NaN
10            11      7   16  1977     5      DS    F  NaN
11            12      7   16  1977     7      DM    M  NaN
12            13      7   16  1977     3      DM    M  NaN
13            14      7   16  1977     8      DM  NaN  NaN
...
[35549 rows x 8 columns]
```
#### Wrapping up before small break 
* Everyone has imported the data?
* How many rows and columns were imported?
* What kind of data is it?



## Manipulating data

Now when we have our data in memory, we can start doing things with it. Firstly, we could check data type of variable `dat`

```python
type(dat)
dat.__class__
dat.dtypes
```

which gives **output**

```
record_id      int64
month          int64
day            int64
year           int64
plot           int64
species       object
sex           object
wgt          float64
dtype: object
```


The `type` function and `__class__` attribute tell us that `dat` is `<class 'pandas.core.frame.DataFrame'>` in Python. This is similar to a spradsheet in excel. The `dtypes` function tells us what columns there are  and what type they are.

### DataFrame object

DataFrame provides all possibilities of R's `data.frame` and  much more. It could store a mix of data types, e.g.characters, integers, facors. It has multiple methods which simplify access to data.

#### Useful methods
* `.columns` - names of columns
* `.head()` - displays 5 first rows
* `.tail()` - displays 5 last rows
* `.shape` - gives shape of  data in tuple (rows, columns)

### Indexing
If we want to get a single value from the **DataFrame** object we must provide an index to it in square brackets and use iloc function.

```python
dat.iloc[2,6]
```

which gives **output**
```
'F'
```

You have to remeber that in Python indexing run from 0. Index like (2, 6) selects a single element of an array. We can also select whole sections as well. For example, we can select month, day and year (columns form second to fourth) of values for the first three rows(rows) like this:

```python
dat.iloc[0:3, 1:4]
```
which gives **output**
```
   month  day  year
0          1      7   16  1977
1          2      7   16  1977
2          3      7   16  1977
```

Slice 1:3 means "Start at index 1 and go to index 3, but not include values at index 4".

We can also use built-in function range to take regurally spaced rows and columns.
In this example we get rows 1, 3 and column 1, 3 and 5

```python
dat.iloc[range(1, 7, 2), range(1, 7, 2)]
```

which gives **output**
```
   month  year species
1      8  1977      DM
3      8  1977      DM
```

__EXERCISES__


## Calculating statistics


We've gotten our data in Python, so that we can do some analytics with it.
First, let's get a sense of our data in file surveys.csv
We might for instance want to know how many animals we trapped in each plot, or how many of each species were caught.
We can look at one column in diifferent ways. We can refere tha column by its number:

```python
dat.iloc[:,7]
```

or by name:

```python
dat.month
dat['month']
```

If you forget the column names, you can type

```python
dat.columns.values
```

which gives **output**:

```
array(['record_id', 'month', 'day', 'year', 'plot', 'species', 'sex', 'wgt'], dtype=object)
```


So, let's get a list of all the species.
The pandas.unique function tells us all the unique names in that column.

```python
pandas.unique(dat.species)
```

Now let's see how many of each species we have:

```python
dat.record_id.groupby(dat.species).nunique()
```

We could even assign it to a variable and make it a DataFrame to make it easier to look at:

```python
species_table = dat.record_id.groupby(dat.species).nunique()
```

Maybe we also want to see how many animals were captured in each plot

```python
dat['plot'].groupby(dat.species).nunique()
```

Now we want to do some actual calculations with the data though.
Let's calculate the average weight of all the animals. Python pandas has a finction describe, that give a lot of statistical informations, like mean, median, max, min, std and count. Describe can be olny used on numeric column.

```python
dat['wgt'].describe()
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
dtype: float64
```

Also we can use just one of this functions:

```python
dat['wgt'].min()
dat[wgt'].max()
dat['wgt'].mean()
dat['wgt'].std()
dat['wgt'].count()
```


Because data is in a vector, when we want to know how much of something we have we ask how long it is with the len() function.

```python
len(dat['wgt'])
```

## Statistics on subsets of data

When analyzing data, though, we often want to look at partial statistics, such as the maximum value per species or the average value per plot.
One way to do this is to select the data we want to create a new temporary array.

```python
dat[dat.species == 'DO']
```

We could see in our table from before that 'DO' had 3027 species.
Let's check to see if that's what we have by checking the number of rows:

```python
dat.record_id.groupby(dat['species']).nunique()['DO']
```

## FUNCTIONS
