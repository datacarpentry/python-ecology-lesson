---
layout: page
root: .
title: Python for Ecologists
subtitle: Instructor's Guide
---



## [Short Introduction to Programming in Python](00-short-introduction-to-Python.md)

## [Starting With Data](01-starting-with-data.md)

Solutions to exercises:

> ### Useful Ways to View DataFrame objects in Python
> 
> Try out the methods below to see what they return.
>
> 1. `surveys_df.columns`.
> 2. `surveys_df.head()`. Also, what does `surveys_df.head(15)` do?
> 3. `surveys_df.tail()`.
> 4. `surveys_df.shape`. Take note of the output of the shape method. What 
>  format does it return the shape of the DataFrame in?

1. `surveys_df.columns` returns the column indices.
2. `surveys_df.head()` prints the first 5 (or n) rows of data.
3. `surveys_df.tail()` prints the last 5 rows of data.
4. `surveys_df.shape` returns a tuple with the number of rows and columns.


> ### Calculating Statistics From Data In A Pandas DataFrame
> Create a list of unique plot ID's found in the surveys data.  Call it 
> plot_names. How many unique plots are there in the data? 
> How many unique species are in the data?

```python
plot_names = pd.unique(surveys_df.plot_id)

print("Number of unique plots: " + str(plot_names.size))
print("Number of unique species: " + str(pd.unique(surveys_df.species_id).size))
```

> ### Groups in Pandas
> 
> 1. How many recorded individuals are female `F` and how many male `M`
> 2. What happens when you group by two columns using the following syntax and
>    then grab mean values:
>        - `sorted2 = surveys_df.groupby(['plot_id','sex'])`
>        - `sorted2.mean()`
> 3. Summarize weight values for each plot in your data. HINT: you can use the
>    following syntax to only create summary statistics for one column in your 
>    data `by_plot['weight'].describe()`

1. There are 15690 female and 17348 male individuals in the dataset. There are 
   several ways to each to those number, e.g. using `sorted.describe()` or 
   `sorted.record_id.count()`.

2. One gets the average values for male and female individuals for each plot.

3. Summarize weight values for each plot:

```python
by_plot = surveys_df.groupby('plot_id')
by_plot['weight'].describe()
```


## [Indexing, Slicing and Subsetting DataFrames in Python](02-index-slice-subset.md)

## [Data Types and Formats](03-data-types-and-format.md)

## [Combining DataFrames with pandas](04-merging-data.md)

## [Data workflows and automation](05-loops-and-functions.md)

## [Plotting Your Data - Matplotlib](06-plotting-with-matplotlib.md)

## [Data Ingest & Visualization - Matplotlib & Pandas](07-putting-it-all-together.md)

## [Accessing SQLite Databases Using Python & Pandas](08-working-with-sql.md)
