##Checking your data

One of the most basic functions in which we might be interested is to make sure our data are what we think they are. If we have some code that changes a certain number to another number, this will only work when all our values are numbers. 

Remember that in base python we can check the type of an object like this:

```UNIX
type()
```

In pandas, checking the dtype of a column is easy. The basic pseudocode looks like this:

```UNIX
df[column_name].dtype
```
An example would be:

```python
df['record_id'].dtype
dtype('int64')
```

where 'df' is whatever name you gave your data frame.

'int64' might be a little bit unusual. We've seen int in our novice materials, with an integer being a whole number. int64 can hold large numbers; in fact int64 holds as many number as a Nintendo64 can hold. This type of precision might not always be important to you, but in certain mathematical operations, this may be very important. If we have a column that contains both ints and floats, Pandas will default to float for the whole column, so as not to lose the decimal points.

Please see the table below for different, common data types:

|Name of Pandas type | Function | Base Python Equivalent |
|------------|---------|-------------------------|
|Object | The most general dtype. Will be assigned to your column if column has mixed types (numbers and strings). | String | 
|int64 | Numerical characters. 64 refers to the memory allocated to hold this character. | Int. |
| float64 | Numerical characters with decimals. If a column contains numbers and NaNs(see below), pandas will default to float64, in case your missing value has a decimal. | float |
|datetime64, timedelta[ns] | Values meant to hold time data. Look into these for time series experiments. | -- |


We probably don't want to examine the dtype of each column by hand. We can easily automate this. 

```python
for col in df:
    print col, df[col].dtypes
record_id int64
day int64
year int64
plot int64
species object
sex object
wgt float64
```

In this way, we can do a simple sanity check: Are our data what we thought? If not, we might want to refer to the [Masking]() section to investigate ways to remove unexpected values. 

Weight is a characteristic that we might want to use in future calculations, like approximations of metabolic rate. We might want these values to be integers. Using Pandas' apply functionality, transforming these values looks like this:

```python
df['wgt'] = df['wgt'].astype('float64')

df['record_id'].dtype
dtype('int64')
```

Back the train up. We did some weird stuff there. The first thing we did was cast each value as a float64. If we use these in further calculations, Python will save the results as floats, **even if the other values involved are ints. Maybe clarify this? Not sure what you mean by 'other values involved'.**

**wgt was already type float64. where does record_id come into this?**

You might wonder why we still have NaN values. *NaN* values are values that cannot be represented mathematically, or are undefined. Pandas, for example, will read an empty cell in a CSV or Excel sheet as a NaN. NaNs have some desirable properties: if we were to average the 'wgt' column without replacing our NaNs, we would get something like this:

```python
df['wgt'].mean()
42.672428212991356
```

But if we were to filter the NaNs and turn them into zeroes (after making a copy of the data so we don't lose our work), we would get something like this:

```python
df1 = df
df1['wgt'] = df1['wgt'].fillna(0)

df1['wgt'].mean()
38.751976145601844
```

While not a large difference, this might be important to the math we'd like to do with our values. When deciding how to manage missing data, it's important to think about how these data will be used. For example, we could fill our missing values with the column average value:

```python
 df1['wgt'] = df['wgt'].fillna(df['wgt'].mean())
```

But what would be an appropriate situation in which to do this? Pandas gives us many options; it's up to us to find the appropraite ones for our work. Download a few data sets from a commonly-used data repository in your field and have a look at how missing data is represented. In Pandas, values that are not numbers and are not NaN can cause your calculations to fail. Choosing a missing data representation is a function of 
+ How your data will be read and understood by others
and
+ How your data will be read and understood by the computer.

##Recap

What we've learned:

+ How to ensure your data types are what you think they are
+ What NaN values are, how they might be represented, and what this means for your work
+ How to replace NaN values, if desired








