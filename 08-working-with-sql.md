---
layout: lesson
root: .
title: Accessing SQLite Databases Using Python & Pandas
---

## Objectives

- Query an sqlite3 database using Python
- Read the result of an SQL query into a pandas DataFrame
- Understand the difference in performance when interacting with data stored as
  CSV vs SQLite
- Understand the benefits of accessing data using a database compared to CSVs


## Python and SQL

When you open a CSV in python, and assign it to a variable name, you are using 
your computers memory to save that variable. Accessing data from a database like 
SQL is not only more efficient, but also it allows you to subset and import only 
the parts of the data that you need.

In the following lesson,
we'll see some approaches that can be taken to do so.

### The `sqlite3` module

The [sqlite3] module provides a straightforward interface for interacting with
SQLite databases.

[sqlite3]: https://docs.python.org/2.7/library/sqlite3.html

```python
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/portal_mammals.sqlite")

cur = con.cursor()

# the result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM species;'):
    print row

#Be sure to close the connection.
con.close()
```

## Accessing data stored in SQLite using Python and Pandas

Using pandas, we can import results of a SQLite query into a dataframe. Note that 
you can use the same SQL commands / syntax that we used in the SQLite lesson. An 
example of using pandas together with sqlite is below:

```python
import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("data/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * from surveys", con)

# verify that result of SQL query is stored in the dataframe
print df.head()

con.close()
```

## Storing data: CSV vs SQLite

Storing your data in an SQLite database can provide substantial performance
improvements when reading/writing compared to CSV. The difference in performance
becomes more noticable as the size of the dataset grows (see for example [these
benchmarks]).

[these benchmarks]: http://sebastianraschka.com/Articles/sqlite3_database.html#benchmarks


## Challenges

1. Create a query that contains survey data collected between 1998 - 2001
 for observations of sex "male" or "female" that includes observation's genus and 
species and plot type for the sample. How many records are returned? 

2. Create a dataframe that contains the total number of observations (count) 
made for all years, and sum of observation weights for each plot, ordered by 
plot ID. 
