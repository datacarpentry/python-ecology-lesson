# Combining DataFrames with pandas

In many "real world" situations, the data we want to use come in multiple files, which we usually load into memory as mutiple pandas DataFrames. However, since many analysis tools expect the data to be in a single DataFrame, we need ways of combining multiple DataFrames together. The pandas package provides [various methods for combining DataFrames](http://pandas.pydata.org/pandas-docs/stable/merging.html).


#Learning Objectives
* Learn how to concatenate two DataFrames together (append one dataFrame to a second dataFrame)
* Learn how to join two DataFrames together using a uniqueID found in both DataFrames


To work through the examples below, we first need to load the species and surveys files into pandas DataFrames. In iPython:

```python
In  [1]: import pandas as pd
In  [2]: surveys_df = pd.read_csv('data/surveys.csv', keep_default_na=False, na_values=[""])
In  [3]: species_df = pd.read_csv('data/species.csv', keep_default_na=False, na_values=[""])

In  [4]: surveys_df
Out [4]:
       record_id  month  day  year  plot species  sex  wgt
0              1      7   16  1977     2      NA    M  NaN
1              2      7   16  1977     3      NA    M  NaN
2              3      7   16  1977     2      DM    F  NaN
3              4      7   16  1977     7      DM    M  NaN
4              5      7   16  1977     3      DM    M  NaN
...          ...    ...  ...   ...   ...     ...  ...  ...
35544      35545     12   31  2002    15      AH  NaN  NaN
35545      35546     12   31  2002    15      AH  NaN  NaN
35546      35547     12   31  2002    10      RM    F   14
35547      35548     12   31  2002     7      DO    M   51
35548      35549     12   31  2002     5     NaN  NaN  NaN

[35549 rows x 8 columns]


In  [5]: species_df
Out [5]:
   species_id             genus          species                   taxa
0          AB        Amphispiza        bilineata                   Bird
1          AH  Ammospermophilus          harrisi    Rodent-not censused
2          AS        Ammodramus       savannarum                   Bird
3          BA           Baiomys          taylori                 Rodent
4          CB   Campylorhynchus  brunneicapillus                   Bird
..        ...               ...              ...                    ...
50         UR            Rodent              sp.                 Rodent
51         US           Sparrow              sp.                   Bird
52         XX               NaN              NaN  Zero Trapping Success
53         ZL       Zonotrichia       leucophrys                   Bird
54         ZM           Zenaida         macroura                   Bird

[55 rows x 4 columns]
```

# Concatenating DataFrames

We can use the `concat` function in Pandas to append either columns or rows from one DataFrame to another.  

	#read in first 10 lines of surveys table
	surveySub = surveys_df.head(10)
	#grab the last 10 rows (minus the last one)
	surveySubLast10 = surveys_df[-10:-1]
	

When we concatenate DataFrames, we need to specify the axis. `axis=0` tells Pandas to stack the second DataFrame under the first one. It will automatically detect whether the column names are the same and will stack accordingly. `axis=0` will stack the columns in the second DataFrame to the RIGHT of the first DataFrame

	#stack the DataFrames on top of each other
	pd.concat([surveySub, surveySubLast10], axis=0)
	#Place the DataFrames side by side
	pd.concat([surveySub, surveySubLast10], axis=1)



# Joining DataFrames

One common way to combine DataFrames is to use columns in each dataset that contain common values. The process of combining DataFrames in this way is called "joining", and the columns containing the common values are called "join key(s)".  Joining DataFrames in this way is often useful when one DataFrame is a "lookup table" containing additional data that we want to include in the other. 

NOTE: This process of joining tables is similar to what we do with tables in SQL!

To better understand joins, let's grab the first 10 lines of our data as a subset to work with. We'll use the `.head` attribute to do this. We'll also read in a subset of the species table. 

	#read in first 10 lines of surveys table
	surveySub = surveys_df.head(10)
	
	speciesSub = pd.read_csv('data/biology/speciesSubset.csv', keep_default_na=False, na_values=[""])

In this example, "speciesSub" is the lookup table containing genus, species, and taxa names that we want to join with the data in "surveySub" to produce a new DataFrame that contains all the columns from both "species_df" *and* "survey_df".


## Identifying join keys

To identify appropriate join keys we first need to know which field(s) are shared between the files (DataFrames). We might inspect both DataFrames to identify these columns. If we are lucky, both DataFrames will have columns with the same name that also contain the same data. If we are less lucky, we need to identify a (differently-named) column in each DataFrame that contains the same information.

```python
	speciesSub.columns
	surveySub.columns
```

In our example, the join key is the column containing the two-letter species identifier, which is called `species` in `surveys_df` and `species_id` in `species_df`.


## Inner joins

There are [different types of joins.](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/).

The most common type of join is called an _inner join_. An inner join combines two DataFrames based on a join key and returns a new DataFrame that contains only those rows that have matching values in *both* of the original DataFrames.


The pandas function for performing joins is called `merge` and is invoked as follows:

```python
	merged_inner = pd.merge(left=surveys_df, right=species_df, left_on='species', right_on='species_id')

	merged_inner
	#what's the size of the output data?
	merged_inner.shape
	merged_inner
```

**OUTPUT:**

 	record_id 	month 	day 	year 	plot 	species_x 	sex 	wgt 	species_id 	genus 	species_y 	taxa
0 	1 	7 	16 	1977 	2 	NL 	M 	NaN 	NL 	Neotoma 	albigula 	Rodent
1 	2 	7 	16 	1977 	3 	NL 	M 	NaN 	NL 	Neotoma 	albigula 	Rodent
2 	3 	7 	16 	1977 	2 	DM 	F 	NaN 	DM 	Dipodomys 	merriami 	Rodent
3 	4 	7 	16 	1977 	7 	DM 	M 	NaN 	DM 	Dipodomys 	merriami 	Rodent
4 	5 	7 	16 	1977 	3 	DM 	M 	NaN 	DM 	Dipodomys 	merriami 	Rodent
5 	8 	7 	16 	1977 	1 	DM 	M 	NaN 	DM 	Dipodomys 	merriami 	Rodent
6 	9 	7 	16 	1977 	1 	DM 	F 	NaN 	DM 	Dipodomys 	merriami 	Rodent
7 	7 	7 	16 	1977 	2 	PE 	F 	NaN 	PE 	Peromyscus 	eremicus 	Rodent


	

Inner joins yield a DataFrame that contains only rows where the value being joins exists in BOTH tables. An example of an inner join, adapted from [this page](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is below:

![Inner join -- courtesy of codinghorror.com](http://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877702708970c-pi.png)

The result of an inner join of `surveySub` and `speciesSub` is a new DataFrame that contains the combined set of columns from `surveySub` and `speciesSub` but *only* those rows that have matching two-letter species codes in both. In other words, if a row in `surveySub` has a value of `species` that does *not* appear in the `species_id` column of `species`, it will not be included in the DataFrame returned by an inner join.  Similarly, if a row in `speciesSub` has a value of `species_id` that does *not* appear in the `species` column of `surveySub`, that row will not be included in the DataFrame returned by an inner join.

The two DataFrames we want to join are passed to the `merge` function using the `left` and `right` argument; for inner joins, which DataFrame is passed using the `left` argument and which is passed using `right` does not matter.

The `left_on='species'` argument tells `merge` to use the `species` column as the join key from `surveySub` (the `left` DataFrame). Similarly , the `right_on='species_id'` argument tells `merge` to use the `species_id` column as the join key from `speciesSub` (the `right` DataFrame).

The result `merged_inner` DataFrame contains all the columns from `surveySub` (record id, month, day, etc.) as well as all the columns from `speciesSub` (species id, genus, species, and taxa). Because both original DataFrames contain a column named `species`, pandas automatically appends a `_x` to the column name from the `left` DataFrame and a `_y` to the column name from the `right` DataFrame.

Notice that `merged_inner` has fewer rows than `surveys_df`. This is an indication that there were rows in `surveys_df` with value(s) for `species` that do not exist as value(s) for `species_id` in `species_df`.


## Left joins

What if we want to add information from `speciesSub` to `surveysSub` without losing any of the information from `surveySub`? In this case, we use a different type of join called a "left outer join", or more briefly, a "left join".

Like an inner join, a left join uses join keys to combine two DataFrames. Unlike an inner join, a left join will return *all* the rows from the `left` DataFrame, even those rows whose join key(s) do not have values in the `right` DataFrame.  Rows in the `left` DataFrame that are missing values for the join key(s) in the `right` DataFrame will simply have null (i.e., NaN or None) values for those columns in the resulting joined DataFrame.

Note: a left join will still discard rows from the `right` DataFrame that do not have values for the join key(s) in the `left` DataFrame.

![Left Join](http://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b01287770273e970c-pi.png)

A left join is performed in pandas by calling the same `merge` function used for inner join, but using the `how='left'` argument:

```python
merged_left = pd.merge(left=surveys_df, right=species_df, how='left', left_on='species', right_on='species_id')

merged_left

OUTPUT: 
 	record_id 	month 	day 	year 	plot 	species_x 	sex 	wgt 	species_id 	genus 	species_y 	taxa
0 	1 	7 	16 	1977 	2 	NL 	M 	NaN 	NL 	Neotoma 	albigula 	Rodent
1 	2 	7 	16 	1977 	3 	NL 	M 	NaN 	NL 	Neotoma 	albigula 	Rodent
2 	3 	7 	16 	1977 	2 	DM 	F 	NaN 	DM 	Dipodomys 	merriami 	Rodent
3 	4 	7 	16 	1977 	7 	DM 	M 	NaN 	DM 	Dipodomys 	merriami 	Rodent
4 	5 	7 	16 	1977 	3 	DM 	M 	NaN 	DM 	Dipodomys 	merriami 	Rodent
5 	8 	7 	16 	1977 	1 	DM 	M 	NaN 	DM 	Dipodomys 	merriami 	Rodent
6 	9 	7 	16 	1977 	1 	DM 	F 	NaN 	DM 	Dipodomys 	merriami 	Rodent
7 	6 	7 	16 	1977 	1 	PF 	M 	NaN 	NaN 	NaN 	NaN 	NaN
8 	10 	7 	16 	1977 	6 	PF 	F 	NaN 	NaN 	NaN 	NaN 	NaN
9 	7 	7 	16 	1977 	2 	PE 	F 	NaN 	PE 	Peromyscus 	eremicus 	Rodent
```

The result DataFrame from a left join (`merged_left`) looks very much like the result DataFrame from an inner join (`merged_inner`) in terms of the columns it contains. However, unlike `merged_inner`, `merged_left` contains the **same number of rows** as the original `surveysSub` DataFrame. When we inspect `merged_left`, we find there are rows where the information that should have come from `speciesSub` (i.e., `species_id`, `genus`, `species_y`, and `taxa`) is missing (they contain NaN values):

```python
	merged_left[ pd.isnull(merged_left.species_id) ]
	#Output: 
 	record_id 	month 	day 	year 	plot 	species_x 	sex 	wgt 	species_id 	genus 	species_y 	taxa
7 	6 	7 	16 	1977 	1 	PF 	M 	NaN 	NaN 	NaN 	NaN 	NaN
8 	10 	7 	16 	1977 	6 	PF 	F 	NaN 	NaN 	NaN 	NaN 	NaN
```

These rows are the ones where the value of `species` from `surveySub` (in this case, `NaN`) does not occur in `speciesSub`.


## Other joins types

The pandas `merge` function supports two other join types:

* Right (outer) join: Invoked by passing `how='right'` as an argument. Similar to a left join, except *all* rows from the `right` DataFrame are kept, while rows from the `left` DataFrame without matching join key(s) values are discarded.

* Full (outer) join: Invoked by passing `how='outer'` as an argument. This join type returns the all pairwise combinations of rows from both DataFrames; i.e., the result DataFrame will contain rows `(left_1, right_1)`, `(left_1, right_2)`, `(left_2, right_1)`, `(left_2, right_2)`, etc. This join type is very rarely used.

#Challenge
Create a new DataFrame by joining the contents of the surveys.csv and species.csv tables. Then calculate and plot the distribution of  

1. taxa by plot 
2. taxa by sex by plot  


# WOULD LIKE TO COME UP WIHT A FEW OTHER CHALLENGE ACTIVITIES
