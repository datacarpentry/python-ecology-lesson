---
title: ' Extra Challenges'
---

A collection of challenges that have been either removed from 
or not (yet) added to the main lesson.

## 06-loops-and-functions

## 03-index-slice-subset

::::::::::::::::::::::::::::::::::::::: challenge

## Additional slicing challenge

You can also select every Nth row by providing a third number inside the `[]`, 
e.g. `surveys_df[1:10:2]` returns every other row in the DataFrame, 
from the second to the tenth:

```output
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  weight
1          2      7   16  1977        3         NL   M             33.0     NaN
3          4      7   16  1977        7         DM   M             36.0     NaN
5          6      7   16  1977        1         PF   M             14.0     NaN
7          8      7   16  1977        1         DM   M             37.0     NaN
9         10      7   16  1977        6         PF   F             20.0     NaN
```


Given this, what do you think will happen when you run `surveys_df[::-1]`?
After you have predicted the result, run the code to see if you were correct.

::::::::::::::::::::::: solution

`surveys_df[::-1]` provides every row of the DataFrame, in reverse order.

::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Looping Over DataFrame

The file `surveys.csv` in the `data` folder contains 25 years of data from surveys,
starting from 1977. We can extract data corresponding to each year in this DataFrame
to individual CSV files, by using a `for` loop:

```python
import pandas as pd

# Load the data into a DataFrame
surveys_df = pd.read_csv('data/surveys.csv')

# Loop through a sequence of years and export selected data
start_year = 1977
end_year = 2002
for year in range(start_year, end_year+1):

    # Select data for the year
    surveys_year = surveys_df[surveys_df.year == year]

    # Write the new DataFrame to a CSV file
    filename = 'data/surveys' + str(year) + '.csv'
    surveys_year.to_csv(filename)
```

What happens if there is no data for a year in a sequence? For example,
imagine we used `1976` as the `start_year`

:::::::::::::::  solution

## Solution

We get the expected files for all years between 1977 and 2002,
plus an empty `data/surveys1976.csv` file with only the headers.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::


