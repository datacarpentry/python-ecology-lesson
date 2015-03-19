# Data Types and Formats

The format of individual columns and rows will impact analysis performed on the data. For example, you can't perform mathematical calculations on string (character formatted) data. This might seem obvious, but numeric values can import into python as a string format. In turn, when you try to perform calculations on the numeric data, you get an error telling you they are strings.

In this lesson we will review ways to explore and better understand our data.

##Learning Objectives

* Learn about character and numeric datatypes
* Learn how to explore the structure of your data 
* Understand NaN values and different ways to deal with them.


##Checking the format of our data
Let's begin by looking at commands that we can use to explore the format of our data. We'll be working with the same surveys.csv dataset that we've used in previous lessons.

```python
#note the pd.read_csv is used because we imported pandas as pd
surveys_df=pd.read_csv("data/biology/surveys.csv")
``` 

**OUTPUT:**

	pandas.core.frame.DataFrame

Remember that in base python we can check the type of an object like this:

```Python
type(surveys_df)
```

We can also check the type of data stored within each column in a Dataframe. 

#Types of Data

Let's begin by talking about data types. How information is stored in a DataFrame or a python object affects what we can do with it. 

#Numberic Formats
For example, we can store numbers as integers or floats. A floating point number is one that can have decimal points even if that decimal point value is 0. For example: 1.13, 2.0 1234.345. If we have a column that contains both ints and floats, Pandas will default to float for the whole column, so as not to lose the decimal points.

On the other hand, an integer will never have a decimal point. Thus 1.13 would be stored as 1. It is efficient for computers to store information using different formats - however why this is done is beyond the scope of this workshop.

And the Int64  (which stands for 64 bit integer) part simply refers to the range of values that can be stored in each cell as follows:

* Int16: -32,768 to +32,767
* Int32: -2,147,483,648 to +2,147,483,647
* Int64: -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807

## Character Formats 
Objects, known as strings in Pandas, are values that contain numbers and / or characters. For example, a string might be a word, a sentence or several sentences. A string might also be a plot name - ie 'plot1'. A string can also contain numbers. However **strings that contain numbers can not be used for mathematical operations**!  


Pandas and base Python call objects slight different names. For example a Pandas object is a string in python. Please see the table below for a translation between the two for 3 common data types:

|Name of Pandas type | Function | Base Python Equivalent |
|------------|---------|-------------------------|
|Object | The most general dtype. Will be assigned to your column if column has mixed types (numbers and strings). | String | 
|int64 | Numerical characters. 64 refers to the memory allocated to hold this character. | Int. |
| float64 | Numerical characters with decimals. If a column contains numbers and NaNs(see below), pandas will default to float64, in case your missing value has a decimal. | float |
|datetime64, timedelta[ns] | Values meant to hold time data. Look into these for time series experiments. | -- |

## Exploring Data in Python and Pandas

Next, let's look at the structure of our surveys data. In pandas, we can check the type of one column in a DataFrame using the syntax `dataFrameName[column_name].dtype`:

```Python
surveys_df['sex'].dtype

```
**OUTPUT:** 

dtype('O')

A type 'O' just stands for "object" which in Pandas world is a string (characters). 


```Python

surveys_df['record_id'].dtype

```

**OUTPUT:** 

dtype('int64')

Int 64, is a 64 bit integer. 

We can use the `dat.dtypes` command to view the data type for each column in a DataFrame. 

	surveys_df.dtypes

which gives **output**:

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
Note that most of the columns in the data are of type `int64`. This means that they are 64 bit integers. But the wgt column is a floating point value which means it contains decimals. 


## Working With Integers and floats 

So we've learned that computers store numbers in one of two ways: as integers or as floating-point numbers (or floats). Integers are the numbers we usually count with. Floats have fractional parts (decimal places).  Addition, subtraction and multiplication work on both as we'd expect, but division works differently. 

	print 5+5
	10

	print 24-4
	20

If we divide one integer by another, we get the quotient without the remainder. In the example below, 9 goes into 5 as an integer 0 times.

	print 5/9
	0

	print 10/3
	3


If either part of the division is a float, on the other hand, the computer creates a floating-point answer:

	print '10.0/3 is:', 10.0/3
	10.0/3 is: 3.33333333333

The computer does this for historical reasons: integer operations were much faster on early machines, and this behavior is actually useful in a lot of situations. It's still confusing, though, so Python 3 produces a floating-point answer when dividing integers if it needs to. We're still using Python 2.7 in this class, though, so if we want 5/9 to give us the right answer, we have to write it as 5.0/9, 5/9.0, or some other variation.

Another way to create a floating-point answer is to explicitly tell the computer that you desire one. This is achieved by casting one of the numbers:

	print 'float(10)/3 is:', float(10)/3

We can also convert a floating point number to an int. Notice that Python by default rounds down when it converts from floating point to integer.

	a=7.33
	int(a)
	7

	b=7.89
	int(b)
	7

# Working With Our Survey Data

Getting back to our data, we can modify the format if we want. For instance, we could convert the `record_id` field to floating point values. 

```python
surveys_df['record_id'] = surveys_df['record_id'].astype('float64')
surveys_df['record_id'].dtype
```

**OUTPUT:**

dtype('float64')


But what if we wanted to convert weight values to integers? 

	surveys_df['wgt'].astype('int')

Notice that this throws a value error `ValueError: Cannot convert NA to integer`.  If we look at the wgt column in the surveys data we notice there are NaN (**N**ot **a** **N**umber) values. *NaN* values are undefined values that cannot be represented mathematically. Pandas, for example, will read an empty cell in a CSV or Excel sheet as a NaN. NaNs have some desirable properties: if we were to average the 'wgt' column without replacing our NaNs, Python would know to skip over those cells.

```python
surveys_df['wgt'].mean()
42.672428212991356
```

## Missing Data Values - NaN 
Dealing with missing data values is always a challenge. It's sometimes hard to know why values are missing - was it because of a data entry error? Or data that someone was unable to collect? And how are missing values represented in the dataset itself.

For instance, in some fields, like Remote Sensing, missing data values are often defined as -9999. Having a bunch of -9999 values in your data could really alter numeric calculations! Often in spreadsheets, cells are left empty where no data are available. Python will, by default replace those missing values with NaN.

Let's explore the NaN values in our data a bit further.

 Using the tools we learned in lesson 02, we can figure out how many rows contain NaN values for weight. We could also create a new subset from our data that only contains rows with weight values >= 0. 

	len(surveys_df[pd.isnull(surveys_df.wgt)])
	#how many rows have wgt values?
	len(surveys_df[surveys_df.wgt>=0])


We could replace all NaN values with zeroes using the `.fillna()' method (after making a copy of the data so we don't lose our work. 

	df1 = surveys_df
	#fill all NaN values with 0
	df1['wgt'] = df1['wgt'].fillna(0)

Then, we can calculate a mean that is different from the mean calculated with the NaN entries ignored: 

```python

df1['wgt'].mean()
38.751976145601844
```

We can fill NaN values with any value that we chose. The code below fills all NaN values with a mean for all wgt values.

```python
 df1['wgt'] = df['wgt'].fillna(df['wgt'].mean())
```

We could also chose to create a subset of our data, only keeping rows that do not contains NaN values. 

The point of this is we need to make conscious decisions about how to manage missing data. This is where we think about how our data will be used and how these values will impact the scientific conclusions made from the data.

Python gives us all of the tools that we need to account for these issues. We just need to be cautious, about how the decisions that we make, impact scientific results.


##Recap

What we've learned:

+ How to explore the data types of columns within a DataFrame
+ How to change the data type 
+ What NaN values are, how they might be represented, and what this means for your work
+ How to replace NaN values, if desired



# Need to build challenge lessons or something to make this lesson more interesting.

#don't love this lesson as is