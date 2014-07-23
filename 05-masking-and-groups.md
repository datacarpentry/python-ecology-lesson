#Grouping

Often, our data contain natural groupings and patterns. In our example data, one such set of groupings might be that of 'male' and 'female'. Pandas has a native function, groupby(), that allows us to specify data groupings.

```python

sorted = df.groupby('sex')
sorted.groups
        record_id        day         year       plot        wgt
sex                                                            
F    18036.412046  16.007138  1990.644997  11.440854  42.170555
M    17754.835601  16.184286  1990.480401  11.098282  42.995379
P    22488.000000  21.000000  1995.000000   8.000000  13.000000
R    21704.000000  12.000000  1994.000000  12.000000        NaN
Z    23839.000000  15.000000  1996.000000   3.000000  18.000000


```

What is returned here is a set of average values for each of our columns for each of our groups. What this also tells us is that there are some weird extra values in this column. Unless we're working with butterflies, Z is unlikely to be a sex. There are different ways in which we might choose to manage that issue. See our section on indexing for more on replacing individual values (and the OS module on how not to overwrite your original data set!). 


