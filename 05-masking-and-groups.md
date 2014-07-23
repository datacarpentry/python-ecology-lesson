Slicing and Masking in pd
====

Goals:
----
* Load data from csv
* Display data where values contain interesting values
* Use masks
* Group data into natural groupings.

open python 
```python
>>> import pandas as pd
```
Read in the data set and store it in a `DataFrame` called "mydata"
```python
>>> mydata = pd.read_csv("data/surveys.csv")
```
`mydata` now contains all of your data from the csv file.

In this data set the dates range from 1977 to 2002. Print only the 2002 values 
```python
>>> mydata[mydata.year == 2002]
````

Which produces the following output:

````python
       record_id  month  day  year  plot species  sex  wgt
33320      33321      1   12  2002     1      DM    M   44
33321      33322      1   12  2002     1      DO    M   58
33322      33323      1   12  2002     1      PB    M   45
33323      33324      1   12  2002     1      AB  NaN  NaN
33324      33325      1   12  2002     1      DO    M   29
33325      33326      1   12  2002     2      OT    F   26
33326      33327      1   12  2002     2      OT    M   24
33327      33328      1   12  2002     2      OT    F   22
33328      33329      1   12  2002     2      DM    M   47
33329      33330      1   12  2002     2      DO    M   51
33330      33331      1   12  2002     2      PE    F   23
33331      33332      1   12  2002     2      OT    F   18
33332      33333      1   12  2002     2      OT    M   25
33333      33334      1   12  2002     2      OT    F   22
33334      33335      1   12  2002     2      DO    F   46
33335      33336      1   12  2002     2      DM    F   45
33336      33337      1   12  2002     2      PB    M   47
33337      33338      1   12  2002     2      PB    F   30
33338      33339      1   12  2002     2     NaN  NaN  NaN
33339      33340      1   12  2002    12      DO    M   24
33340      33341      1   12  2002    12      PE    F   15
33341      33342      1   12  2002    12      DO    F   26
33342      33343      1   12  2002    12      DO    F   47
33343      33344      1   12  2002    12      DM    M   40
33344      33345      1   12  2002    12      DO    M   55
33345      33346      1   12  2002    12      PE    M   23
33346      33347      1   12  2002    12      DM    F   45
33347      33348      1   12  2002    19      PB    M   51
33348      33349      1   12  2002    19      PB    M   46
33349      33350      1   12  2002    19      PP    F   13
...          ...    ...  ...   ...   ...     ...  ...  ...
35519      35520     12   31  2002     9      SF  NaN   36
35520      35521     12   31  2002     9      DM    M   48
35521      35522     12   31  2002     9      DM    F   45
35522      35523     12   31  2002     9      DM    F   44
35523      35524     12   31  2002     9      PB    F   27
35524      35525     12   31  2002     9      OL    M   26
35525      35526     12   31  2002     8      OT    F   24
35526      35527     12   31  2002    13      DO    F   43
35527      35528     12   31  2002    13      US  NaN  NaN
35528      35529     12   31  2002    13      PB    F   25
35529      35530     12   31  2002    13      OT    F  NaN
35530      35531     12   31  2002    13      PB    F  NaN
35531      35532     12   31  2002    14      DM    F   43
35532      35533     12   31  2002    14      DM    F   48
35533      35534     12   31  2002    14      DM    M   56
35534      35535     12   31  2002    14      DM    M   53
35535      35536     12   31  2002    14      DM    F   42
35536      35537     12   31  2002    14      DM    F   46
35537      35538     12   31  2002    15      PB    F   31
35538      35539     12   31  2002    15      SF    M   68
35539      35540     12   31  2002    15      PB    F   23
35540      35541     12   31  2002    15      PB    F   31
35541      35542     12   31  2002    15      PB    F   29
35542      35543     12   31  2002    15      PB    F   34
35543      35544     12   31  2002    15      US  NaN  NaN
35544      35545     12   31  2002    15      AH  NaN  NaN
35545      35546     12   31  2002    15      AH  NaN  NaN
35546      35547     12   31  2002    10      RM    F   14
35547      35548     12   31  2002     7      DO    M   51
35548      35549     12   31  2002     5     NaN  NaN  NaN

[2229 rows x 8 columns]
```

This shows that there are 2,229 values where the year is 2002.

Now print all data where the year is NOT 2002.

```python
>>> mydata[mydata.year!=2002]
```

Which produces the following output:

```python
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
14            15      7   16  1977     6      DM    F  NaN
15            16      7   16  1977     4      DM    F  NaN
16            17      7   16  1977     3      DS    F  NaN
17            18      7   16  1977     2      PP    M  NaN
18            19      7   16  1977     4      PF  NaN  NaN
19            20      7   17  1977    11      DS    F  NaN
20            21      7   17  1977    14      DM    F  NaN
21            22      7   17  1977    15     NaN    F  NaN
22            23      7   17  1977    13      DM    M  NaN
23            24      7   17  1977    13      SH    M  NaN
24            25      7   17  1977     9      DM    M  NaN
25            26      7   17  1977    15      DM    M  NaN
26            27      7   17  1977    15      DM    M  NaN
27            28      7   17  1977    11      DM    M  NaN
28            29      7   17  1977    11      PP    M  NaN
29            30      7   17  1977    10      DS    F  NaN
...          ...    ...  ...   ...   ...     ...  ...  ...
33290      33291     12   15  2001    23      PE    M   18
33291      33292     12   15  2001    23      RM    F    8
33292      33293     12   15  2001    20      PE    F   22
33293      33294     12   15  2001    20      SH    M   43
33294      33295     12   15  2001    20      PB    F   33
33295      33296     12   15  2001    20      PB    M   35
33296      33297     12   15  2001    20      RM    M   11
33297      33298     12   15  2001    20      RM    F    8
33298      33299     12   15  2001    20      PB    F   28
33299      33300     12   15  2001    20      PB    F   30
33300      33301     12   15  2001    20      PB    F   31
33301      33302     12   15  2001    24      PE    M   24
33302      33303     12   15  2001    24      PE    M   23
33303      33304     12   15  2001    24      RM    M   10
33304      33305     12   15  2001     7      PB    M   44
33305      33306     12   15  2001     7      OT    M   21
33306      33307     12   15  2001     7      OT    M   19
33307      33308     12   15  2001     7      PP    M   16
33308      33309     12   16  2001     3     NaN  NaN  NaN
33309      33310     12   16  2001     4     NaN  NaN  NaN
33310      33311     12   16  2001     5     NaN  NaN  NaN
33311      33312     12   16  2001     6     NaN  NaN  NaN
33312      33313     12   16  2001     8     NaN  NaN  NaN
33313      33314     12   16  2001     9     NaN  NaN  NaN
33314      33315     12   16  2001    10     NaN  NaN  NaN
33315      33316     12   16  2001    11     NaN  NaN  NaN
33316      33317     12   16  2001    13     NaN  NaN  NaN
33317      33318     12   16  2001    14     NaN  NaN  NaN
33318      33319     12   16  2001    15     NaN  NaN  NaN
33319      33320     12   16  2001    16     NaN  NaN  NaN

[33320 rows x 8 columns]
```

This shows that there are 33,320 values where the year is not 2002.

Now print all values where the year is between 1980-1985 (inclusive)

```python
>>> mydata[(mydata.year>=1980) & (mydata.year<=1985)]
```

Which produces the following output::

```python
       record_id  month  day  year  plot species  sex  wgt
2270        2271      1   15  1980     8      DO    M   53
2271        2272      1   15  1980    11      PF    F   10
2272        2273      1   15  1980    18      DM    F   33
2273        2274      1   15  1980    11      DM    M   37
2274        2275      1   15  1980     8      DO    F   29
2275        2276      1   15  1980    11      DS    M  132
2276        2277      1   15  1980     8      PF    M    8
2277        2278      1   15  1980     9      OT    M   23
2278        2279      1   15  1980    11      DM    F   36
2279        2280      1   15  1980    21      OT    F   21
2280        2281      1   15  1980    11      OL    M   29
2281        2282      1   15  1980    17      DM    F   49
2282        2283      1   15  1980    11      OL    M   23
2283        2284      1   15  1980     9      OL    M   32
2284        2285      1   15  1980    10      OL    F   24
2285        2286      1   15  1980    11      DM    M   47
2286        2287      1   15  1980    21      OT    M   22
2287        2288      1   15  1980    19      RM    F   12
2288        2289      1   15  1980    20      DS    F  150
2289        2290      1   15  1980    11      DM    M   49
2290        2291      1   15  1980     9      OL    F   34
2291        2292      1   15  1980    12      DM    F   40
2292        2293      1   15  1980    18      DS    F  132
2293        2294      1   15  1980    22      DM    F   25
2294        2295      1   15  1980     9      OL    M   36
2295        2296      1   15  1980     8      DO    F   50
2296        2297      1   15  1980    11      DM    M   45
2297        2298      1   15  1980    17      DM    M   47
2298        2299      1   15  1980     9      DM    M   46
2299        2300      1   15  1980    18      DM    F   29
...          ...    ...  ...   ...   ...     ...  ...  ...
11197      11198     12    8  1985     4      DS    M  129
11198      11199     12    8  1985     8      DM    F   42
11199      11200     12    8  1985     7      AB  NaN  NaN
11200      11201     12    8  1985     5      OL    M   29
11201      11202     12    8  1985     9      DM    F   39
11202      11203     12    8  1985     7      PE    F   19
11203      11204     12    8  1985     3      PP    F   16
11204      11205     12    8  1985     5      DO    M   56
11205      11206     12    8  1985    11      DM    F   38
11206      11207     12    8  1985     2      PE    M   19
11207      11208     12    8  1985     8      DS    F  120
11208      11209     12    8  1985     2      DO    F   52
11209      11210     12    8  1985     2      DM    F   40
11210      11211     12    8  1985    13      DM    M   45
11211      11212     12    8  1985     4      DS  NaN  121
11212      11213     12    8  1985    13      AH  NaN  NaN
11213      11214     12    8  1985     1      DM    F   44
11214      11215     12    8  1985     2     NaN    F  160
11215      11216     12    8  1985     3      RM    M    9
11216      11217     12    8  1985     4      OL    M   34
11217      11218     12    8  1985     9      DM    F   39
11218      11219     12    8  1985     8      DM    F   41
11219      11220     12    8  1985     5      DO    F   56
11220      11221     12    8  1985    13      AH  NaN  NaN
11221      11222     12    8  1985     7      AB  NaN  NaN
11222      11223     12    8  1985     4      DM    M   40
11223      11224     12    8  1985    11      DM    M   49
11224      11225     12    8  1985     7      PE    M   18
11225      11226     12    8  1985     1      DM    M   47
11226      11227     12    8  1985    15     NaN  NaN  NaN

[8957 rows x 8 columns]
```

Now print all values where the year is greater than 1985 but less than 1988 (1986-1987)

```python
[(mydata.year>1985) & (mydata.year<1988)]
```
Which produces the following output:
```python
       record_id  month  day  year  plot species  sex  wgt
11227      11228      3    8  1986    12      DS    M  119
11228      11229      3    8  1986    23      DO    F   56
11229      11230      3    8  1986    21      RM    F   11
11230      11231      3    8  1986    16      RM    M    9
11231      11232      3    8  1986    12     NaN    F  170
11232      11233      3    8  1986     6      DM    F   52
11233      11234      3    8  1986    24      DM    M   48
11234      11235      3    8  1986    21      RM    F   10
11235      11236      3    8  1986     6      DM    M   46
11236      11237      3    8  1986    16      RM    F   10
11237      11238      3    8  1986    17      DM    F   38
11238      11239      3    8  1986    12      OT    M   26
11239      11240      3    8  1986     6      DS    M  130
11240      11241      3    8  1986    24      DO    F   52
11241      11242      3    8  1986    20      DM    F   48
11242      11243      3    8  1986    12      DO  NaN  NaN
11243      11244      3    8  1986    14      OL    M   37
11244      11245      3    8  1986     6      OL    F   31
11245      11246      3    8  1986    21      PE    F   25
11246      11247      3    8  1986    14      DM    F   39
11247      11248      3    8  1986    20      DM    M   47
11248      11249      3    8  1986    12      DO    M  NaN
11249      11250      3    8  1986    17      OL    M   34
11250      11251      3    8  1986    12      DM    M   46
11251      11252      3    8  1986    24      DM    F   41
11252      11253      3    8  1986    22      DM    F   43
11253      11254      3    8  1986    17      DO    M   53
11254      11255      3    8  1986    12      DO    M   49
11255      11256      3    8  1986    22      DM    M   45
11256      11257      3    8  1986    16      OL  NaN  NaN
...          ...    ...  ...   ...   ...     ...  ...  ...
13810      13811     11   22  1987    10      RM    M    9
13811      13812     11   22  1987     1      DM    F   41
13812      13813     11   22  1987     7      RM    F    7
13813      13814     11   22  1987     1      OL    M   27
13814      13815     11   22  1987    15     NaN    F  190
13815      13816     11   22  1987    13      DM    F  NaN
13816      13817     11   22  1987     3      PE    M   23
13817      13818     11   22  1987     4      OL    F   29
13818      13819     11   22  1987    15      PE    M   20
13819      13820     11   22  1987     2      DM    M   45
13820      13821     11   22  1987    15      RM    M   12
13821      13822     11   22  1987     2      DM    M   38
13822      13823     11   22  1987    11      DM    M   27
13823      13824     11   22  1987     4      DM    M   35
13824      13825     11   22  1987    11      PE    M   24
13825      13826     11   22  1987    10      AH  NaN  NaN
13826      13827     11   22  1987     9     NaN    M  204
13827      13828     11   22  1987     2      UP  NaN  NaN
13828      13829     11   22  1987    13      AB  NaN  NaN
13829      13830     11   22  1987     1      DO    M   40
13830      13831     11   22  1987     2      PE    F   27
13831      13832     11   22  1987    15      AB  NaN  NaN
13832      13833     11   22  1987     4      DM    M   43
13833      13834     11   22  1987     3      PE    M   22
13834      13835     11   22  1987     4      DS    M  134
13835      13836     11   22  1987     5      PM    M   27
13836      13837     11   22  1987    11      DM    F   40
13837      13838     11   22  1987     1      DM    M   52
13838      13839     11   22  1987     8      DM    M   35
13839      13840     11   22  1987    13      DM    F   38

[2613 rows x 8 columns]
```



Using Masks
----

A mask can be useful to locate where values are NaN, or "Not a Number"

```python
>>> pd.isnull(mydata)
```

Which produces the following output:

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
12        False  False  False  False  False   False  False   True
13        False  False  False  False  False   False   True   True
14        False  False  False  False  False   False  False   True
15        False  False  False  False  False   False  False   True
16        False  False  False  False  False   False  False   True
17        False  False  False  False  False   False  False   True
18        False  False  False  False  False   False   True   True
19        False  False  False  False  False   False  False   True
20        False  False  False  False  False   False  False   True
21        False  False  False  False  False    True  False   True
22        False  False  False  False  False   False  False   True
23        False  False  False  False  False   False  False   True
24        False  False  False  False  False   False  False   True
25        False  False  False  False  False   False  False   True
26        False  False  False  False  False   False  False   True
27        False  False  False  False  False   False  False   True
28        False  False  False  False  False   False  False   True
29        False  False  False  False  False   False  False   True
...         ...    ...    ...    ...    ...     ...    ...    ...
35519     False  False  False  False  False   False   True  False
35520     False  False  False  False  False   False  False  False
35521     False  False  False  False  False   False  False  False
35522     False  False  False  False  False   False  False  False
35523     False  False  False  False  False   False  False  False
35524     False  False  False  False  False   False  False  False
35525     False  False  False  False  False   False  False  False
35526     False  False  False  False  False   False  False  False
35527     False  False  False  False  False   False   True   True
35528     False  False  False  False  False   False  False  False
35529     False  False  False  False  False   False  False   True
35530     False  False  False  False  False   False  False   True
35531     False  False  False  False  False   False  False  False
35532     False  False  False  False  False   False  False  False
35533     False  False  False  False  False   False  False  False
35534     False  False  False  False  False   False  False  False
35535     False  False  False  False  False   False  False  False
35536     False  False  False  False  False   False  False  False
35537     False  False  False  False  False   False  False  False
35538     False  False  False  False  False   False  False  False
35539     False  False  False  False  False   False  False  False
35540     False  False  False  False  False   False  False  False
35541     False  False  False  False  False   False  False  False
35542     False  False  False  False  False   False  False  False
35543     False  False  False  False  False   False   True   True
35544     False  False  False  False  False   False   True   True
35545     False  False  False  False  False   False   True   True
35546     False  False  False  False  False   False  False  False
35547     False  False  False  False  False   False  False  False
35548     False  False  False  False  False    True   True   True

[35549 rows x 8 columns]
```

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

#Grouping

Often, our data contain natural groupings and patterns. In our example data, one such set of groupings might be that of 'male' and 'female'. pd has a native function, groupby(), that allows us to specify data groupings.

```python

>>>sorted = df.groupby('sex')
>>>sorted.groups
        record_id        day         year       plot        wgt
sex                                                            
F    18036.412046  16.007138  1990.644997  11.440854  42.170555
M    17754.835601  16.184286  1990.480401  11.098282  42.995379
P    22488.000000  21.000000  1995.000000   8.000000  13.000000
R    21704.000000  12.000000  1994.000000  12.000000        NaN
Z    23839.000000  15.000000  1996.000000   3.000000  18.000000


```

What is returned here is a set of average values for each of our columns for each of our groups. What this also tells us is that there are some weird extra values in this column. Unless we're working with butterflies, Z is unlikely to be a sex. There are different ways in which we might choose to manage that issue. See our section on indexing for more on replacing individual values (and the OS module on how not to overwrite your original data set!). 


