
#Indexing, Slicing and Subsetting DataFrames in Python
In lesson 01, we covered reading a CSV into python using Pandas. We learned how to save the data as an object with a variable name, how to perform basic math on the data, how to calculate summary stats and how to create plots of the data.

In this lesson, we will explore ways to subset and access different parts of the data through indexing, slicing and subsetting. 

## Learning Objectives

*  Learn about 0-based indexing in Python
*  Learn about numeric vs label based indexes
*  Learn how to select subsets of data from a DataFrame using Slicing and Indexing methods
*  Understand what a boolean object is and how it can be used to "mask" or identify particular sets of values within another object.


## Making Sure Our Data Are Loaded

We will continue to use the surveys dataset that we worked with in the last exercise. Just in case you've closed it, let's reopen it using Pandas.

```python
#first make sure pandas is loaded
import pandas as pd
#read in the surveys csv
pd.read_csv("data/surveys.csv")
```

# Extracting and Viewing Slices of our DataFrame - Indexing & Slicing in Python
We often want to work with subsets of our  **DataFrame** object. There are different ways to accomplish this, using labels (column headings), numeric ranges or specific x,y index locations. 


##Selecting Data Using Labels (Column Headings)

We use square brackets `[]` to select a subset of an Python object. For example, we can select a column within the surveys DataFrame by name:

	dat['species']
	#the syntax below gives you the same output
	dat.species

We can also create an object with a variable name that is a subset of a dataset we are working with. 
	#create an object named surveys_species that just contains the species column from the dat DataFrame
	surveys_species=dat['species']

We can pass a list of columns to select columns in that order. This is useful for applying a function (like transform) to a subset of your columns.  NOTE: If a column name is not contained in the DataFrame, an exception (error) will be raised. 
	
	#select the species and plot columns from the DataFrame
	surveys[['species', 'plot']]

We can also access columns within DataFrames as an attribute:

	dat.wgt

##Extracting Range based Subsets: Slicing 

### REMINDER: Python Uses 0-based Indexing

Before we dig into python, let's remind ourselves that Python uses 0-based indexing. This means that the first element in an object is located at position 0. This is different from other tools like R and Matlab that index objects starting at 1. 

	#quick review:
	a=[1,2,3,4,5]
	#what value does the comment below return?
	a[0]
	#how about this command:
	a[5]
	#or this
	a[len(a)]

##Slicing Subsets of Rows in Python

Slicing using the [] operator selects a set of rows and/or columns from a DataFrame. To slice out a set of rows, you use the following syntax:  `data[start:stop]`. When slicing in pandas the start bound is included in the output. The stop bound is one step BEYOND the row you want to select. SO if you want to select rows 0, 1 and 2 your code would look like this: included. data[0:3]. 

The stop bound in Python is different from what you might be used to in languages like Matlab and R.

	#select the first, second and third rows from the surveys variable
	dat[0:3]
	#select the first 5 rows (not including row with the index value of 6)
	dat[:5]
	#select the second to last row
	dat[-1:]


We can also create new objects by slicing out parts of a DataFrame. 

	#copy the surveys dataframe
	surveys_copy=dat
	
	#set the first three rows of data in the dataframe to 0
	surveys_copy[0:3]=0

## Slicing Subsets of Rows and Columns in Python
To select a subset of rows AND columns from our DataFrame, we need to use the `iloc` method. For example, we can select month, day and year (columns 2,3 and 4 if we start counting at 1), like this:

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

Notice anything odd about the output above? We asked for a slice that goes from 0:3. Wouldn't that suggest that python would select 4 rows in total? Another unique aspect of python is that when you slice a subset of data from `0:3`, you are actually telling python to start at index 0 and select rows 0,1,2 **up to but not including 3**. This might be confusing at first, but you'll get used to it with time. 


## Index based subsets

We can also select specific ranges of our data in both the row and column direction using the `loc` and `iloc` arguments. The `loc` argument allows you to select data using labels AND numeric integer locations. `iloc` only allows you to select ranges using labels, `loc` only accepts integer index values.

NOTE: Index values and labels must be in the DataFrame or you will get a KeyError. Remember that the start bound and the stop bound are included. When using `loc` Integers can be used, but they refer to the index label and not the position.

	#select all columns for rows of index values 0 and 10
	dat.loc[[0,10],:]
	#what does this do?
	dat.loc[0,['species', 'plot','wgt']]
	
	#What happens when you type the code below?
	dat.loc[[0,10,35549],:]


To do this, we need to provide an index that specifies what part of the data frame we'd like to extract. We can ask for a data value according to the row and column location of the value within the data frame using the `iloc` function: `dat.iloc[row,column]`.


```python
dat.iloc[2,6]
```

which gives **output**
```
'F'
```

Remember that Python indexing begins at 0. So, the index location [2, 6] selects the element that is 3 rows down and 7 columns over in the DataFrame. 

## Challenge Activities

1. What happens when you type:

```python
	surveys[0:3]
	surveys[:5]
	surveys[-1:]
```



Using Masks
----

A mask can be useful to locate where a particular subset of values exist or don't exist - for example,  NaN, or "Not a Number" values. To understand masks, we also need to understand `BOOLEAN` objects in python, so let's cover that first. 

Boolean values include `true` or `false`. So for example 

	#set x to 5
	x=5
	#what does the code below return
	x>5
	#how about this
	x==5
 
When we ask python what the value of x>5 is, we get `False`. This is because x is not greater than 5 it is = 5. This is the fundamental principle behind masks. You can ask python to assess each value in a row or column, and create a new object that returns either true or false values for those values.

Let's start with the `is null` method which asks python to set all cells that have null values to `True`.  


```python
>>> pd.isnull(dat)
```

A snippet of the output is below: 

```python
      record_id  month    day   year   plot species    sex    wgt
0         False  False  False  False  False    True  False   True
1         False  False  False  False  False    True  False   True
2         False  False  False  False  False   False  False   True
3         False  False  False  False  False   False  False   True
4         False  False  False  False  False   False  False   True
5         False  False  False  False  False   False  False   True
6         False  False  False  False  False   False  False   True
7         False  False  False  False  False   False  False   True
8         False  False  False  False  False   False  False   True
9         False  False  False  False  False   False  False   True
10        False  False  False  False  False   False  False   True
11        False  False  False  False  False   False  False   True


[35549 rows x 8 columns]
```

Now this boolean output is interesting, but it becomes powerful when we actually use it as an ides to identify the locations of these NaN values and extract them.

	emptyWeights = dat[pd.isnull(dat.wgt)]

Let's take a minute to look at the statement above. We are using the Boolean object as an index. We are asking python to select rows that have a `NaN` value for weight. 


This can also be accomplished for individual columns

```python
>>> pd.isnull(mydata.year)
```

```python
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10    False
11    False
12    False
13    False
14    False
...
35534    False
35535    False
35536    False
35537    False
35538    False
35539    False
35540    False
35541    False
35542    False
35543    False
35544    False
35545    False
35546    False
35547    False
35548    False
Name: year, Length: 35549, dtype: bool
```

# need some better challenge activities
# is there more that we can do with booleans here???