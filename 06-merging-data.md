# Merging data with pandas

In many "real world" cases, the datasets we want ot use come in multiple files. To make use such data for analyses, we often have to merge them  into a single data frame.


Loading pandas in ipython:
```python
In [1]: import pandas as pd
```

Reading the data from our text files:
```python
In [2]: surveys = pd.read_csv('data/surveys.csv', keep_default_na=False, na_values=[""])
In [3]: species = pd.read_csv('data/species.csv', keep_default_na=False, na_values=[""])
```

Inspect the data frame to identify a "join key" (column common to both data frames). If we're lucky, they'll have the same name in both data frames; otherwise, we'll need some knowledge about the dataset to find one. In this case, the "species" column in the "surveys" dataframe and the "species_id" column in the "species" data frame.
```python
In [4]: surveys
Out[4]:
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


In [5]: species
Out[5]:
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

# Inner joins

Inner join: returns data frame consisting of rows that are present in *both* dataframes. In this example, the result dataframe is missing rows from the "survey" dataframe that do not have a corresponding value in "species" dataframe (evidenced by result having fewer rows than original "surveys" dataframe).

"left_on" argument is name of join key in the left table (surveys); "right_on" argument is name of join key in the right table (species).

*TODO*: explain "left" vs. "right" dataframe arguments (implicit).
```python
In  [6]: merged_inner = pd.merge(surveys, species, left_on='species', right_on='species_id')

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

# Left joins

Left joins: often times, we want to keep all the data from one dataframe while adding information from another. Common use case is the "lookup" table scenario. To do this, we use what's called a left join, which returns all the rows from the original "left" dataframe ("surveys") and rows from the "right" dataframe ("species") if matching join key is found. If no value for the join key on the right dataframe is found, the values in the result dataframe as null/NaN. (*TODO*: show example of null values in code below.)

```python
In  [8]: merged_left = pd.merge(surveys, species, how='left', left_on='species', right_on='species_id')

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

# Other joins

Right join: similar to left join, except it keeps all rows from the "right" table, discards rows 

Full join: returns all rows from both data frame.
