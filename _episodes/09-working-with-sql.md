---
title: Accessing SQLite Databases Using Python and Pandas
teaching: 20
exercises: 25
questions:
    - "What if my data are stored in an SQL database? Can I manage them with Python?"
    - "How can I write data from Python to be used with SQL?"
objectives:
    - "Use the sqlite3 module to interact with a SQL database."
    - "Access data stored in SQLite using Python."
    - "Describe the difference in interacting with data stored as a CSV file versus in SQLite."
    - "Describe the benefits of accessing data using a database compared to a CSV file."
keypoints:
    - "sqlite3 provides a SQL-like interface to read, query, and write SQL databases from Python."
    - "sqlite3 can be used with Pandas to read SQL data to the familiar Pandas DataFrame."
    - "Pandas and sqlite3 can also be used to transfer between the CSV and SQL formats."
---

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

[sqlite3]: https://docs.python.org/3/library/sqlite3.html

~~~
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/portal_mammals.sqlite")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM species;'):
    print(row)

# Be sure to close the connection
con.close()
~~~
{: .language-python}

### Queries

One of the most common ways to interact with a database is by querying:
retrieving data based on some search parameters. Use a SELECT statement string.
The query is returned as a single tuple or a tuple of tuples. Add a WHERE
statement to filter your results based on some parameter.

~~~
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
~~~
{: .language-python}

## Accessing data stored in SQLite using Python and Pandas

Using pandas, we can import results of a SQLite query into a dataframe. Note
that you can use the same SQL commands / syntax that we used in the SQLite
lesson. An example of using pandas together with sqlite is below:

~~~
import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("data/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * from surveys", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()
~~~
{: .language-python}

## Storing data: CSV vs SQLite

Storing your data in an SQLite database can provide substantial performance
improvements when reading/writing compared to CSV. The difference in performance
becomes more noticeable as the size of the dataset grows (see for example [these
benchmarks]).

[these benchmarks]: http://sebastianraschka.com/Articles/2013_sqlite_database.html#results-and-conclusions


> ## Challenge - SQL
>
> 1. Create a query that contains survey data collected between 1998 - 2001 for
>   observations of sex "male" or "female" that includes observation's genus and
>   species and site type for the sample. How many records are returned?
>
> 2. Create a dataframe that contains the total number of observations (count)
>   made for all years, and sum of observation weights for each site, ordered by
>   site ID.
{: .challenge}

## Storing data: Create new tables using Pandas

We can also us pandas to create new tables within an SQLite database. Here, we run we re-do an
exercise we did before with CSV files using our SQLite database. We first read in our survey data,
then select only those survey results for 2002, and then save it out to its own table so we can work
with it on its own later.

~~~
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
~~~
{: .language-python}

> ## Challenge - Saving your work
>
> 1. For each of the challenges in the previous challenge block, modify your code to save the
>   results to their own tables in the portal database.
>
> 2. What are some of the reasons you might want to save the results of your queries back into the
>   database? What are some of the reasons you might avoid doing this.
{: .challenge}

{% include links.md %}

