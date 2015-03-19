#VARIABLES STUFF

For example,

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



# removing the range stuff too-- not relevant in my opinion
#is the stuff below needed? i think it could be confusing. what is the use case for selecting data in this manner?

##Slicing Data Using The Range Function
We can also use built-in function [range](http://www.pythoncentral.io/pythons-range-function-explained/) to take regularly spaced rows and columns. The range function tells python to select a set of values using the following format (startingValue, EndingValue, Step). 

What happens when you run `range(2,6,2)` in python? 

In the example below, we get rows with the index value of 1, 3, 5 and columns with the index value 1, 3 and 5.

```python
dat.iloc[range(1, 7, 2), range(1, 7, 2)]
```

which gives **output**
```
   month  year species
1      8  1977      NL
3      8  1977      DM
5	7   1977	   PF
```


# ASK MARIELA about this... you get the datatype back without this too... maybe we can cut this?

Selection with .ix method

Return the column in question and its data type. Format is [row, column] add in what inputs are, etc


	dat.ix[:,'species']

You can also set variables to your subset of data. this will be a series

	surveys_species=dat.ix[:,'species']

More slicing
 
surveys.ix[100,['species', 'wgt']]



# THIS IS A REALLY RANDOM ADDITION -- pulling it for now...it should be introduced with the shape element
Finally, we might want to weight  data is in a vector, when we want to know how much of something we have we ask how long it is with the len() function.

```python
len(dat['wgt'])
```
# DO WE NEED THIS IF THEY HAVE PANDAS INSTALLED? Should we check to see if pandas is installed.
#also if they are using anaconda it might need to be conda install pandas. i think this belongs in the workshop overview.

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


## Statistics on subsets of data

When analyzing data we often want to look at summary statistics, for subsets of our samples. For instance, we might want to look at the maximum weight per species or the average weight per plot.

One way to do this is to select the data we want to create a new temporary DataFrame. Let's first build our query. Let's find records that are for the species "DO". To do this, we need to first build the query:  `dat.species == 'DO'`. Now, we need to find the rows in our dataFrame that contain DO. to do that we use the syntax `dat[dat.species == 'DO']`. Using this syntax, we are asking Python to pull out all rows where dat.species = DO. 

```python
a=dat[dat.species == 'DO']
#find out how many individuals are of type 'DO'
len(a)
```

The `len` function allows us to determine the length or number of entries that match the `species='DO'` criteria. 3027 individuals collected were of species 'DO'.
