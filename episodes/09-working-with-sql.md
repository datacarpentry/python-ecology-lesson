---
title: Accessing SQLite Databases Using Python and Pandas
teaching: 20
exercises: 25
---

::::::::::::::::::::::::::::::::::::::: objectives

- Use the sqlite3 module to interact with a SQL database.
- Access data stored in SQLite using Python.
- Describe the difference in interacting with data stored as a CSV file versus in SQLite.
- Describe the benefits of accessing data using a database compared to a CSV file.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What if my data are stored in an SQL database? Can I manage them with Python?
- How can I write data from Python to be used with SQL?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Python and SQL

When you open a CSV in python, and assign it to a variable name, you are using
your computers memory to save that variable. Accessing data from a database like
SQL is not only more efficient, but also it allows you to subset and import only
the parts of the data that you need.

In the following lesson, we'll see some approaches that can be taken to do so.

### The `sqlite3` module

The [sqlite3] module provides a straightforward interface for interacting with
SQLite databases. A connection object is created using `sqlite3.connect()`; the
connection must be closed at the end of the session with the `.close()` command.
While the connection is open, any interactions with the database require you to
make a cursor object with the `.cursor()` command. The cursor is then ready to
perform all kinds of operations with `.execute()`.

```python
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/portal_mammals.sqlite")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM species;'):
    print(row)

# Be sure to close the connection
con.close()
```

### Queries

One of the most common ways to interact with a database is by querying:
retrieving data based on some search parameters. Use a SELECT statement string.
The query is returned as a single tuple or a tuple of tuples. Add a WHERE
statement to filter your results based on some parameter.

```python
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/portal_mammals.sqlite")

cur = con.cursor()

# Return all results of query
cur.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
cur.fetchall()

# Return first result of query
cur.execute('SELECT species FROM species WHERE taxa="Bird"')
cur.fetchone()

# Be sure to close the connection
con.close()
```

## Accessing data stored in SQLite using Python and Pandas

Using pandas, we can import results of a SQLite query into a dataframe. Note
that you can use the same SQL commands / syntax that we used in the SQLite
lesson. An example of using pandas together with sqlite is below:

```python
import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("data/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * from surveys", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()
```

## Storing data: CSV vs SQLite

Storing your data in an SQLite database can provide substantial performance
improvements when reading/writing compared to CSV. The difference in performance
becomes more noticeable as the size of the dataset grows (see for example [these
benchmarks][these benchmarks]).

:::::::::::::::::::::::::::::::::::::::  challenge

## Challenge - SQL

1. Create a query that contains survey data collected between 1998 - 2001 for
   observations of sex "male" or "female" that includes observation's genus and
   species and site type for the sample. How many records are returned?
2. Create a dataframe that contains the total number of observations (count)
   made for all years, and sum of observation weights for each site, ordered by
   site ID.

::::::::::::::::::::::: solution

1. 
   ```python
   #Connect to the database
   con = sqlite3.connect("data/portal_mammals.sqlite")
   
   cur = con.cursor()
   
   # Return all results of query: year, plot type (site type), genus, species and sex
   # from the join of the tables surveys, plots and species, for the years 1998-2001 where sex is 'M' or 'F'.
   cur.execute('SELECT surveys.year,plots.plot_type,species.genus,species.species,surveys.sex \
       FROM surveys INNER JOIN plots ON surveys.plot = plots.plot_id INNER JOIN species ON \
       surveys.species = species.species_id WHERE surveys.year>=1998 AND surveys.year<=2001 \
       AND ( surveys.sex = "M" OR surveys.sex = "F")')

   print('The query returned ' + str(len(cur.fetchall())) + ' records.')
   
   # Close the connection
   con.close()
   ```
   
   ```output
   The query returned 5546 records.
   ```
2. 
   ```python
   # Create two sqlite queries results, read as pandas DataFrame
   # Include 'year' in both queries so we have something to merge (join) on.
   con = sqlite3.connect("data/portal_mammals.sqlite")
   df1 = pd.read_sql_query("SELECT year,COUNT(*) FROM surveys GROUP BY year", con)
   df2 = pd.read_sql_query("SELECT year,plot,SUM(wgt) FROM surveys GROUP BY \
           year,plot ORDER BY plot ASC",con)
   
   # Turn the plot_id column values into column names by pivoting
   df2 = df2.pivot(index='year',columns='plot')['SUM(wgt)']
   df = pd.merge(df1, df2, on='year')
   
   # Verify that result of the SQL queries is stored in the combined dataframe
   print(df.head())
   
   con.close()
   ```
   
   ```output
   year  COUNT(*)       1       2       3       4       5       6      7  \
   0  1977       503   567.0   784.0   237.0   849.0   943.0   578.0  202.0   
   1  1978      1048  4628.0  4789.0  1131.0  4291.0  4051.0  2371.0   43.0   
   2  1979       719  1909.0  2501.0   430.0  2438.0  1798.0   988.0  141.0   
   3  1980      1415  5374.0  4643.0  1817.0  7466.0  2743.0  3219.0  362.0   
   4  1981      1472  6229.0  6282.0  1343.0  4553.0  3596.0  5430.0   24.0   
   
        8  ...      15     16      17      18     19      20     21      22  \
   0   595.0  ...    48.0  132.0  1102.0   646.0  336.0   640.0   40.0   316.0   
   1  3669.0  ...   734.0  548.0  4971.0  4393.0  124.0  2623.0  239.0  2833.0   
   2  1954.0  ...   472.0  308.0  3736.0  3099.0  379.0  2617.0  157.0  2250.0   
   3  3596.0  ...  1071.0  529.0  5877.0  5075.0  691.0  5523.0  321.0  3763.0   
   4  4946.0  ...  1083.0  176.0  5050.0  4773.0  410.0  5379.0  600.0  5268.0   
   
      23      24  
   0  169.0     NaN  
   1    NaN     NaN  
   2  137.0   901.0  
   3  742.0  4392.0  
   4   57.0  3987.0  
   
   [5 rows x 26 columns]
   ```

::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Storing data: Create new tables using Pandas

We can also use pandas to create new tables within an SQLite database. Here, we re-do an
exercise we did before with CSV files using our SQLite database. We first read in our survey data,
then select only those survey results for 2002, and then save it out to its own table so we can work
with it on its own later.

```python
import pandas as pd
import sqlite3

con = sqlite3.connect("data/portal_mammals.sqlite")

# Load the data into a DataFrame
surveys_df = pd.read_sql_query("SELECT * from surveys", con)

# Select only data for 2002
surveys2002 = surveys_df[surveys_df.year == 2002]

# Write the new DataFrame to a new SQLite table
surveys2002.to_sql("surveys2002", con, if_exists="replace")

con.close()
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Challenge - Saving your work

1. For each of the challenges in the previous challenge block, modify your code to save the
  results to their own tables in the portal database.

2. What are some of the reasons you might want to save the results of your queries back into the
  database? What are some of the reasons you might avoid doing this.

::::::::::::::::::::::: solution

1. 
   ```python
   #Connect to the database
   con = sqlite3.connect("data/portal_mammals.sqlite")
   
   # Read the results into a DataFrame
   df1 = pd.read_sql_query('SELECT surveys.year,plots.plot_type,species.genus,species.species,surveys.sex \
       FROM surveys INNER JOIN plots ON surveys.plot = plots.plot_id INNER JOIN species ON \
       surveys.species = species.species_id WHERE surveys.year>=1998 AND surveys.year<=2001 \
       AND ( surveys.sex = "M" OR surveys.sex = "F")')

   df1.to_sql("New Table 1", con, if_exists="replace")
   
   # We already have the 'df' DataFrame created in the earlier exercise
   df.to_sql("New Table 2", con, if_exists="replace")
   
   # Close the connection
   con.close()
   ```
2. If the database is shared with others and common queries 
   (and potentially data corrections) are likely to be required by many
   it may be efficient for one person to perform the work 
   and save it back to the database as a new table
   so others can access the results directly instead of performing the query themselves,
   particularly if it is complex.
   
   However, we might avoid doing this if the database is an authoritative source
   (potentially version controlled) which should not be modified by users.
   Instead, we might save the qeury results to a new database that is more appropriate for downstream work.

::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::



[sqlite3]: https://docs.python.org/3/library/sqlite3.html
[these benchmarks]: https://sebastianraschka.com/Articles/2013_sqlite_database.html#results-and-conclusions


:::::::::::::::::::::::::::::::::::::::: keypoints

- sqlite3 provides a SQL-like interface to read, query, and write SQL databases from Python.
- sqlite3 can be used with Pandas to read SQL data to the familiar Pandas DataFrame.
- Pandas and sqlite3 can also be used to transfer between the CSV and SQL formats.

::::::::::::::::::::::::::::::::::::::::::::::::::


