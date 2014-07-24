# Combining DataFrames with pandas

In many "real world" situations, the data we want to use come in multiple files, which we usually load into memory as mutiple pandas DataFrames. However, since many analysis tools expect the data to be in a single DataFrame, we need ways of combining multiple DataFrames together. Fortunately, the pandas package provides [various methods for combining DataFrames](http://pandas.pydata.org/pandas-docs/stable/merging.html).

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

**TODO**: added code and text explaning how to concatenate DataFrames using pandas (i.e., append as additional rows and columns without specific criteria)


# Joining DataFrames

One common way of combining DataFrames is based on common values in one or more columns. The process of combining DataFrames in this way is called "joining", and the columns containing the common values are called "join key(s)".  Joining DataFrames in this way is often useful when one DataFrame is a "lookup table" containing additional data that we want to include in the other.

In this example, "species_df" is the lookup table containing genus, species, and taxa names that we want to join with the data in "survey_df" to produce a new DataFrame that contains all the columns from both "species_df" *and* "survey_df".


## Identifying join keys

Identifying appropriate join keys requires enough knowledge of the dataset to know which field(s) are shared between the files (DataFrames) and inspecting the actual DataFrames to identify the columns that contain those names. If we are lucky, both DataFrames will have columns with the same name that also contain the same data. If we are less lucky, we need to identify a (differently-named) column in each DataFrame that contains the same information.

In our example, the join key is the column containing the two-letter species identifer, which is called `species` in `surveys_df` and `species_id` in `species_df`.


## Inner joins

Probably the most common type of join is called an _inner join_. An inner join combines two DataFrames based on a join key and returns a new DataFrame that contains only those rows that have matching values in *both* of the original DataFrames.

To give a concrete example, the result of an inner join of `surveys_df` and `species_df` is a new DataFrame that contains the combined set of columns from `surveys_df` and `species_df` but *only* those rows that have matching two-letter species codes in both. In other words, if a row in `surveys_df` has a value of `species` that does *not* appear in the `species_id` column of `species`, it will not be included in the DataFrame returned by an inner join.  Similarly, if a row in `species_df` has a value of `species_id` that does *not* appear in the `species` column of `surverys_df`, that row will not be included in the DataFrame returned by an inner join.

The pandas function for performing joins is called `merge` and is invoked as follows:

```python
In  [6]: merged_inner = pd.merge(left=surveys_df, right=species_df, left_on='species', right_on='species_id')

In  [7]: merged_inner
Out [7]:
       record_id  month  day  year  plot species_x  sex  wgt species_id  \
0              1      7   16  1977     2        NA    M  NaN         NA   
1              2      7   16  1977     3        NA    M  NaN         NA   
2             22      7   17  1977    15        NA    F  NaN         NA   
3             38      7   17  1977    17        NA    M  NaN         NA   
4             72      8   19  1977     2        NA    M  NaN         NA   
...          ...    ...  ...   ...   ...       ...  ...  ...        ...   
34781      28988     12   23  1998     6        CT  NaN  NaN         CT   
34782      35512     12   31  2002    11        US  NaN  NaN         US   
34783      35513     12   31  2002    11        US  NaN  NaN         US   
34784      35528     12   31  2002    13        US  NaN  NaN         US   
34785      35544     12   31  2002    15        US  NaN  NaN         US   

               genus species_y     taxa  
0            Neotoma  albigula   Rodent  
1            Neotoma  albigula   Rodent  
2            Neotoma  albigula   Rodent  
3            Neotoma  albigula   Rodent  
4            Neotoma  albigula   Rodent  
...              ...       ...      ...  
34781  Cnemidophorus    tigris  Reptile  
34782        Sparrow       sp.     Bird  
34783        Sparrow       sp.     Bird  
34784        Sparrow       sp.     Bird  
34785        Sparrow       sp.     Bird  

[34786 rows x 12 columns]
```

The two DataFrames we want to join are passed to the `merge` function using the `left` and `right` argument; for inner joins, which DataFrame is passed using the `left` argument and which is passed using `right` does not matter.

The `left_on='species'` argument tells `merge` to use the `species` column as the join key from `surveys_df` (the `left` DataFrame). Similarly , the `right_on='species_id'` argument tells `merge` to use the `species_id` column as the join key from `species_df` (the `right` DataFrame).

The result `merged_inner` DataFrame contains all the columns from `surveys_df` (record id, month, day, etc.) as well as all the columns from `species_df` (species id, genus, species, and taxa). Because both original DataFrames contain a column named `species`, pandas automatically appends a `_x` to the column name from the `left` DataFrame and a `_y` to the column name from the `right` DataFrame.

Notice that `merged_inner` has fewer rows than `surveys_df`. This is an indication that there were rows in `surveys_df` with value(s) for `species` that do not exist as value(s) for `species_id` in `species_df`.


## Left joins

What if we want to add information from `species_df` to `surveys_df` without losing any of the information from `surveys_df`? In this case, we use a different type of join called a "left outer join", or more briefly, a "left join".

Like an inner join, a left join uses join keys to combine two DataFrames. Unlike an inner join, a left join will return *all* the rows from the `left` DataFrame, even those rows whose join key(s) do not have values in the `right` DataFrame.  Rows in the `left` DataFrame that are missing values for the join key(s) in the `right` DataFrame will simply have null (i.e., NaN or None) values for those columns in the resulting joined DataFrame.

Note: a left join will still discard rows from the `right` DataFrame that do not have values for the join key(s) in the `left` DataFrame.

A left join is performed in pandas by calling the same `merge` function used for inner join, but using the `how='left'` argument:

```python
In  [8]: merged_left = pd.merge(left=surveys_df, right=species_df, how='left', left_on='species', right_on='species_id')

In  [9]: merged_left
Out [9]:
       record_id  month  day  year  plot species_x  sex  wgt species_id  \
0              1      7   16  1977     2        NA    M  NaN         NA   
1              2      7   16  1977     3        NA    M  NaN         NA   
2             22      7   17  1977    15        NA    F  NaN         NA   
3             38      7   17  1977    17        NA    M  NaN         NA   
4             72      8   19  1977     2        NA    M  NaN         NA   
...          ...    ...  ...   ...   ...       ...  ...  ...        ...   
35544      28988     12   23  1998     6        CT  NaN  NaN         CT   
35545      35512     12   31  2002    11        US  NaN  NaN         US   
35546      35513     12   31  2002    11        US  NaN  NaN         US   
35547      35528     12   31  2002    13        US  NaN  NaN         US   
35548      35544     12   31  2002    15        US  NaN  NaN         US   

               genus species_y     taxa  
0            Neotoma  albigula   Rodent  
1            Neotoma  albigula   Rodent  
2            Neotoma  albigula   Rodent  
3            Neotoma  albigula   Rodent  
4            Neotoma  albigula   Rodent  
...              ...       ...      ...  
35544  Cnemidophorus    tigris  Reptile  
35545        Sparrow       sp.     Bird  
35546        Sparrow       sp.     Bird  
35547        Sparrow       sp.     Bird  
35548        Sparrow       sp.     Bird  

[35549 rows x 12 columns]
```

The result DataFrame from a left join (`merged_left`) looks very much like the result DataFrame from an inner join (`merged_inner`) in terms of the columns it contains. However, unlike `merged_inner`, `merged_left` contains the same number of rows as the original `surveys_df` DataFrame. When we inspect `merged_left`, we find there are rows where the information that should have come from `species_df` (i.e., `species_id`, `genus`, `species_y`, and `taxa`) is missing:

```python
In [10]: merged_left[ pd.isnull(merged_left.species_id) ]
Out[10]:
       record_id  month  day  year  plot species_x  sex  wgt species_id genus  \
29669        324     10   17  1977     7       NaN  NaN  NaN        NaN   NaN   
29670        325     10   17  1977    10       NaN  NaN  NaN        NaN   NaN   
29671        326     10   17  1977    23       NaN  NaN  NaN        NaN   NaN   
29672        401     11   13  1977     3       NaN  NaN  NaN        NaN   NaN   
29673        402     11   13  1977    15       NaN  NaN  NaN        NaN   NaN   
...          ...    ...  ...   ...   ...       ...  ...  ...        ...   ...   
30427      34757      9   10  2002    23       NaN  NaN  NaN        NaN   NaN   
30428      34970     10    6  2002    10       NaN  NaN  NaN        NaN   NaN   
30429      35188     11   10  2002    10       NaN  NaN  NaN        NaN   NaN   
30430      35385     12    8  2002    10       NaN  NaN  NaN        NaN   NaN   
30431      35549     12   31  2002     5       NaN  NaN  NaN        NaN   NaN   

      species_y taxa  
29669       NaN  NaN  
29670       NaN  NaN  
29671       NaN  NaN  
29672       NaN  NaN  
29673       NaN  NaN  
...         ...  ...  
30427       NaN  NaN  
30428       NaN  NaN  
30429       NaN  NaN  
30430       NaN  NaN  
30431       NaN  NaN  

[763 rows x 12 columns]
```

These rows are the ones where the value of `species` from `surveys_df` (in this case, `NaN`) does not occur in `species_df`.


## Other joins types

The pandas `merge` function supports two other join types:

* Right (outer) join: Invoked by passing `how='right'` as an arguement. Similar to a left join, except *all* rows from the `right` DataFrame are kept, while rows from the `left` DataFrame without matching join key(s) values are discarded.

* Full (outer) join: Invoked by passing `how='outer'` as an argument. This join type returns the all pairwise combinations of rows from both DataFrames; i.e., the result DataFrame will contain rows `(left_1, right_1)`, `(left_1, right_2)`, `(left_2, right_1)`, `(left_2, right_2)`, etc. This join type is very rarely used.
