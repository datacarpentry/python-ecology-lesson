#Indexing and Selecting

We often want to select subsets of data frames and other data types in Python. To select portions of a data type in python, we need to tell python what parts - what columns and or rows - or elements we want to select. We call this process of "indexing" or slicing our data.

#maybe use a series with an index as an example


##Slicing strings

A section of an array is called a slice. We can take slices of character strings as well:

	element = 'oxygen'
	print 'first three characters:', element[0:3]
	print 'last three characters:', element[3:6]


Output:

	first three characters: oxy
	last three characters: gen

What is the value of element[:4]? What about element[4:]? Or element[:]?

What is element[-1]? What is element[-2]? Given those answers, explain what element[1:-1] does.

#Python Uses 0-based Indexing
It is important to note that Python follows what's known as 0 based indexing. this means that the first element in an object is located at position `0`. This is different from other tools like R and Matlab that index objects starting at 1. 

#Add numeric example here...

We will continue to use the surveys dataset that we worked with in the last exercise. Just in case you've closed it, let's reopen it using Pandas.

	#first make sure pandas is loaded
	import pandas as pd
	#read in the surveys csv
	pd.read_csv("data/surveys.csv")



#FIXING ALL OF THIS BELOW -- it's called DAT in the lesson 01
##The Basics

We often use square brackets to select a subset of an Python object: `[]`. For example, we can select a column within the surveys dataframe by name:

	dat['species']

We can also set a variable to be a subset of a dataset we are working with (for example the column containing species data). 

	surveys_species=surveys['species']

You can pass a list of columns to [] to select columns in that order. If a column is not contained in the dataframe, an exception will be raised. This is useful for applying a function (like transform) to a subset of your columns.
	
	surveys[['species', 'plot']]

You can also access columns within DataFrames as an attribute:

	surveys.wgt

##Slicing Ranges

Slicing using the [] operator selects a set of rows or columns from a dataframe. When slicing in pandas the start bound and the stop bound are included. data[start:stop]

	#select the first, second and third rows from the surveys variable
	surveys[0:3]

	surveys[:5]

	surveys[-1:]


You can set values using slices


	surveys_copy=surveys.copy()

	surveys_copy[0:3]=0

Selection with .ix method

Return the column in question and its data type. Format is [row, column] add in what inputs are, etc


	surveys.ix[:,'species']

You can also set variables to your subset of data. this will be a series

	surveys_species=surveys.ix[:,'species']

More slicing
 
surveys.ix[100,['species', 'wgt']]

##Selection by Label

All labels must be in index or a KeyError will be raised. remember that the start bound and the stop bound are included. Integers can be used, but they refer to the index label and not the position.

	surveys.loc[[0,10],:]

	surveys.loc[0,['species', 'plot','wgt']]

Selection by Position

0-based indexing, start bounds included and upper bound excluded. trying to use a non-integer will raise an IndexError


	surveys.iloc[:3]

integer slicing

	surveys.iloc[0:10, 4:6]

slicing rows


	surveys.iloc[0:3,:]

slicing columns

	surveys.iloc[:, 0:5]

integer lists


	surveys.iloc[[2,4,6],[1,3,5]]

can pull out a specific data point

	surveys.iloc[7,156]

