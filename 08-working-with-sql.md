---
layout: lesson
root: .
title: Working with SQL
---

## Objectives

- Query an sqlite3 database using Python
- Read the result of an SQL query into a pandas DataFrame
- Understand the difference in performance when interacting with data stored as
  CSV vs SQLite


## Python and SQL

Python is often used to interact with SQL databases. In the following lesson,
we'll see some approaches that can be taken to do so.

### The `sqlite3` module

The [sqlite3] module provides a straightforward interface for interacting with
SQLite databases.

[sqlite3]: https://docs.python.org/2.7/library/sqlite3.html

```python
import sqlite3

con = sqlite3.connect("data/portal_mammals.sqlite")
cur = connection.cursor()

# the result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM surveys;'):
    print row

con.close()
```

## Python and pandas and SQL

An example of using pandas together with sqlite is shown below:

```python
import pandas as pd
import sqlite3

# Read sqlite data into a pandas DataFrame
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
