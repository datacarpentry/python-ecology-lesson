---
title: Instructor Notes
---

# Challenge solutions

## Install the required workshop packages

Please use the instructions in the [Setup][lesson-setup] document to perform installs. If you
encounter setup issues, please file an issue with the tags 'High-priority'.

## Checking installations.

In the [`episodes/files/scripts/check_env.py`](../episodes/files/scripts/check_env.py) directory, you will find a script called check\_env.py This checks the
functionality of the Anaconda install.

By default, Data Carpentry does not have people pull the whole repository with all the scripts and
addenda. Therefore, you, as the instructor, get to decide how you'd like to provide this script to
learners, if at all.  To use this, students can navigate into `_includes/scripts` in the terminal, and
execute the following:

```bash
python check_env.py
```

If learners receive an `AssertionError`, it will inform you how to help them correct this
installation. Otherwise, it will tell you that the system is good to go and ready for Data
Carpentry!


## 02-starting-with-data

:::::::::::::::::::::::::::::::::::::::::  callout

## Important Bug Note

In Pandas prior to 0.18.1 there is a bug causing `surveys_df['weight'].describe()` to return
a runtime error.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 03-index-slice-subset

Tip: use `.head()` method throughout this lesson to keep your display neater for students.
Encourage students to try with and without `.head()` to reinforce this useful tool and then to use
it or not at their preference. For example, if a student worries about keeping up in pace with
typing, let them know they can skip the `.head()`, but that you'll use it to keep more lines of
previous steps visible.

## 04-data-types-and-format

### Writing Out Data to CSV

If the students have trouble generating the output, or anything happens with that, the folder
[`sample_output`](https://github.com/datacarpentry/python-ecology-lesson/tree/main/sample_output)
in this repository contains the file `surveys_complete.csv` with the data they should generate.

## 05-merging-data

- In the data folder, there are two survey data files: survey2001.csv and survey2002.csv. Read the
  data into Python and combine the files to make one new data frame. Create a plot of average plot
  weight by year grouped by sex. Export your results as a CSV and make sure it reads back into
  Python properly.

```python
# read the files:
survey2001 = pd.read_csv("data/survey2001.csv")
survey2002 = pd.read_csv("data/survey2002.csv")
# concatenate
survey_all = pd.concat([survey2001, survey2002], axis=0)
# get the weight for each year, grouped by sex:
weight_year = survey_all.groupby(['year', 'sex']).mean()["wgt"].unstack()
# plot:
weight_year.plot(kind="bar")
plt.tight_layout()  # tip(!)
```

![](fig/04_chall_weight_year.png){alt='average weight for each year, grouped by sex'}

```python
# writing to file:
weight_year.to_csv("weight_for_year.csv")
# reading it back in:
pd.read_csv("weight_for_year.csv", index_col=0)
```

- Create a new DataFrame by joining the contents of the surveys.csv and species.csv tables.

```python
merged_left = pd.merge(left=surveys_df,right=species_df, how='left', on="species_id")
```

Then calculate and plot the distribution of:

**1\. taxa per plot** (number of species of each taxa per plot):

Species distribution (number of taxa for each plot) can be derived as follows:

```python
merged_left.groupby(["plot_id"])["taxa"].nunique().plot(kind='bar')
```

![](fig/04_chall_ntaxa_per_site.png){alt='taxa per plot'}

*Suggestion*: It is also possible to plot the number of individuals for each taxa in each plot
(stacked bar chart):

```python
merged_left.groupby(["plot_id", "taxa"]).count()["record_id"].unstack().plot(kind='bar', stacked=True)
plt.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.05))
```

(the legend otherwise overlaps the bar plot)

![](fig/04_chall_taxa_per_site.png){alt='taxa per plot'}

**2\. taxa by sex by plot**:
Providing the Nan values with the M|F values (can also already be changed to 'x'):

```python
merged_left.loc[merged_left["sex"].isnull(), "sex"] = 'M|F'
```

Number of taxa for each plot/sex combination:

```python
ntaxa_sex_site= merged_left.groupby(["plot_id", "sex"])["taxa"].nunique().reset_index(level=1)
ntaxa_sex_site = ntaxa_sex_site.pivot_table(values="taxa", columns="sex", index=ntaxa_sex_site.index)
ntaxa_sex_site.plot(kind="bar", legend=False)
plt.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.08),
           fontsize='small', frameon=False)
```

![](fig/04_chall_ntaxa_per_site_sex.png){alt='taxa per plot per sex'}

*Suggestion (for discussion only)*:

The number of individuals for each taxa in each plot per sex can be derived as well.

```python
sex_taxa_site  = merged_left.groupby(["plot_id", "taxa", "sex"]).count()['record_id']
sex_taxa_site.unstack(level=[1, 2]).plot(kind='bar', logy=True)
plt.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.15),
           fontsize='small', frameon=False)
```

![](fig/04_chall_sex_taxa_site_intro.png){alt='taxa per plot per sex'}

This is not really the best plot choice: not readable,... A first option to make this better, is to
make facets. However, pandas/matplotlib do not provide this by default. Just as a pure matplotlib
example (`M|F` if for not-defined sex records):

```python
fig, axs = plt.subplots(3, 1)
for sex, ax in zip(["M", "F", "M|F"], axs):
    sex_taxa_site[sex_taxa_site["sex"] == sex].plot(kind='bar', ax=ax, legend=False)
    ax.set_ylabel(sex)
    if not ax.is_last_row():
        ax.set_xticks([])
        ax.set_xlabel("")
axs[0].legend(loc='upper center', ncol=5, bbox_to_anchor=(0.5, 1.3),
              fontsize='small', frameon=False)
```

![](fig/04_chall_sex_taxa_site.png){alt='taxa per plot per sex'}

However, it would be better to link to [Seaborn][seaborn] and [Altair][altair] for its kind of
multivariate visualisations.

- In the data folder, there is a plot CSV that contains information about the type associated with
  each plot. Use that data to summarize the number of plots by plot type.

```python
plot_info = pd.read_csv("data/plots.csv")
plot_info.groupby("plot_type").count()
```

- Calculate a diversity index of your choice for control vs rodent exclosure plots. The index should
  consider both species abundance and number of species. You might choose the simple biodiversity
  index described here which calculates diversity as `the number of species in the plot / the total number of individuals in the plot = Biodiversity index.`

```python
merged_site_type = pd.merge(merged_left, plot_info, on='plot_id')
# For each plot, get the number of species for each plot
nspecies_site = merged_site_type.groupby(["plot_id"])["species"].nunique().rename("nspecies")
# For each plot, get the number of individuals
nindividuals_site = merged_site_type.groupby(["plot_id"]).count()['record_id'].rename("nindiv")
# combine the two series
diversity_index = pd.concat([nspecies_site, nindividuals_site], axis=1)
# calculate the diversity index
diversity_index['diversity'] = diversity_index['nspecies']/diversity_index['nindiv']
```

Making a bar chart:

```python
diversity_index['diversity'].plot(kind="barh")
plt.xlabel("Diversity index")
```

![](fig/04_chall_diversity_index.png){alt='taxa per plot per sex'}

## 07-visualization-ggplot-python

Note `plotnine` contains a *lot* of deprecation warnings in some versions of python/matplotlib, warnings may need to be supressed with

```python
import warnings
warnings.filterwarnings(action='once')
```

iPython notebooks for plotting can be viewed in the `learners` folder.

## 08-putting-it-all-together

Answers are embedded with challenges in this lesson, other than random distribtuion which is left to the learner to choose, and final plot, for which the learner should investigate the matplotlib gallery.

Scientists often operate on mathematical equations. Being able to use them in their graphics has a
lot of added value. Luckily, Matplotlib provides powerful tools for text control. One of them is the
ability to use LaTeX mathematical notation, whenever text is used (you can learn more about LaTeX
math notation here: [https://en.wikibooks.org/wiki/LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)). To use mathematical
notation, surround your text using the dollar sign ("$").  LaTeX uses the backslash character ("\\")
a lot. Since backslash has a special meaning in the Python strings, you should replace all the
LaTeX-related backslashes with two backslashes.

```python
plt.plot(t, t, 'r--', label='$y=x$')
plt.plot(t, t**2 , 'bs-', label='$y=x^2$')
plt.plot(t, (t - 5)**2 + 5 * t - 0.5, 'g^:', label='$y=(x - 5)^2 + 5  x - \\frac{1}{2}$') # note the double backslash

plt.legend(loc='upper left', shadow=True, fontsize='x-large')

# Note the double backslashes in the line below.
plt.xlabel('This is the x axis. It can also contain math such as $\\bar{x}=\\frac{\\sum_{i=1}^{n} {x}} {N}$')
plt.ylabel('This is the y axis')
plt.title('This is the figure title')

plt.show()
```

[This page][matplotlib-mathtext] contains more information.

## 09-working-with-sql

### Challenge - SQL

- Create a query that contains survey data collected between 1998 - 2001 for observations of sex "male" or "female" that includes observation's genus and species and site type for the sample. How many records are returned?

```python
#Connect to the database
con = sqlite3.connect("data/portal_mammals.sqlite")

cur = con.cursor()

# Return all results of query: year, plot type (site type), genus, species and sex
# from the join of the tables surveys, plots and species, for the years 1998-2001 where sex is 'M' or 'F'.
cur.execute('SELECT surveys.year,plots.plot_type,species.genus,species.species,surveys.sex \
  FROM surveys INNER JOIN plots ON surveys.plot_id = plots.plot_id INNER JOIN species ON \
  surveys.species_id = species.species_id WHERE surveys.year>=1998 AND surveys.year<=2001 \
  AND ( surveys.sex = "M" OR surveys.sex = "F")')

print(len(cur.fetchall()))

# Close the connection
con.close()
```

```output
5546
```

Answer: 5546 records are found.

- Create a dataframe that contains the total number of observations (count) made for all years, and sum of observation weights for each site, ordered by site ID.

This question is a little ambiguous but we could e.g. do two SQL queries into dataframes, then pivot the second and merge them to create a table of observation count and plot total weight per year. The PIVOT operation could alternatively be performed in SQL.

```python
import pandas as pd
import sqlite3

# Create two sqlite queries results, read as pandas DataFrame
# Include 'year' in both queries so we have something to merge (join) on.
con = sqlite3.connect("data/portal_mammals.sqlite")
df1 = pd.read_sql_query("SELECT year,COUNT(*) FROM surveys GROUP BY year", con)
df2 = pd.read_sql_query("SELECT year,plot_id,SUM(weight) FROM surveys GROUP BY \
        year,plot_id ORDER BY plot_id ASC",con)

# Turn the plot_id column values into column names by pivoting
df2 = df2.pivot(index='year',columns='plot_id')['SUM(weight)']
df = pd.merge(df1, df2, on='year')

# Verify that result of the SQL queries is stored in the combined dataframe
print(df.head())

con.close()
```

Output looks something like

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
```

### Challenge - Saving your work

- For each of the challenges in the previous challenge block, modify your code to save the results to their own tables in the portal database.

Per the example in the lesson, create a variable for the results of the SQL query, then add something like

```python
<new_table>.to_sql("New Table", con, if_exists="replace")
```

- What are some of the reasons you might want to save the results of your queries back into the database? What are some of the reasons you might avoid doing this?

If the database is shared with others and common queries (and potentially data corrections) are likely to be required by many it may be efficient for one person to perform the work and save it back to the database as a new table so others can access the results directly instead of performing the query themselves, particularly if it is complex.
However, we might avoid doing this if the database is an authoritative source (potentially version controlled) which should not be modified by users. Instead, we might save the qeury results to a new database that is more appropriate for downstream work.

[seaborn]: https://stanford.edu/~mwaskom/software/seaborn
[altair]: https://github.com/ellisonbg/altair
[matplotlib-mathtext]: https://matplotlib.org/users/mathtext.html



