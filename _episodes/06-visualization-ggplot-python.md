---
title: Making Plots With ggplot
teaching: 40
exercises: 50
questions:
    - " How can I visualize data in Python?"
    - " What is 'grammar of graphics'?"
objectives:
    - "Create a ggplot object."
    - "Set universal plot settings."
    - "Modify an existing ggplot object."
    - "Change the aesthetics of a plot such as colour."
    - "Edit the axis labels."
    - "Build complex plots using a step-by-step approach."
    - "Create scatter plots, box plots, and time series plots."
    - "Use the facet_wrap and facet_grid commands to create a collection of plots splitting the data by a factor variable."
    - "Create customized plot styles to meet their needs."
---

## Disclaimer ##
 Python has powerful built-in plotting capabilities such as `matplotlib`, but for this exercise, we will be using the [`ggplot`](http://ggplot.yhathq.com/) package, which facilitates the creation of highly-informative plots of structured data based on the R implementation of [`ggplot2`](http://ggplot2.org/) and [The Grammar of Graphics](http://link.springer.com/book/10.1007%2F0-387-28695-0) by Leland Wilkinson.




```python
import pandas as pd


surveys_complete = pd.read_csv('data_output/surveys_complete.csv')
surveys_complete
```


```python
%matplotlib inline
from ggplot import *
```


# Plotting with ggplot

We will make the same plot using the `ggplot` package.

`ggplot` is a plotting package that makes it simple to create complex plots
from data in a dataframe. It uses default settings, which help creating
publication quality plots with a minimal amount of settings and tweaking.

ggplot graphics are built step by step by adding new elements.

To build a ggplot we need to:

- bind the plot to a specific data frame using the `data` argument




- define aesthetics (`aes`), by selecting the variables to be plotted and the variables to define the presentation
     such as plotting size, shape color, etc.,




```python
ggplot( aesthetics= aes(x = 'weight', y = 'hindfoot_length'), data = surveys_complete)
```


- add `geoms` -- graphical representation of the data in the plot (points,
     lines, bars). To add a geom to the plot use `+` operator:




```python
ggplot( aes(x = 'weight', y = 'hindfoot_length'), data = surveys_complete) + geom_point()
```


The `+` in the `ggplot2` package is particularly useful because it allows you
to modify existing `ggplot` objects. This means you can easily set up plot
"templates" and conveniently explore different types of plots, so the above
plot can also be generated with code like this:




```python
# Create
surveys_plot = ggplot( aes(x = 'weight', y = 'hindfoot_length'), data = surveys_complete)

# Draw the plot
surveys_plot + geom_point()
```


Notes:

- Anything you put in the `ggplot()` function can be seen by any geom layers
  that you add (i.e., these are universal plot settings). This includes the x and
  y axis you set up in `aes()`.
- You can also specify aesthetics for a given geom independently of the
  aesthetics defined globally in the `ggplot()` function.


# Building your plots iteratively

Building plots with ggplot is typically an iterative process. We start by
defining the dataset we'll use, lay the axes, and choose a geom.




```python
ggplot(aes(x = 'weight', y = 'hindfoot_length'), data = surveys_complete, ) + geom_point()
```


Then, we start modifying this plot to extract more information from it. For
instance, we can add transparency (alpha) to avoid overplotting.




```python
ggplot(aes(x = 'weight', y = 'hindfoot_length'), data = surveys_complete) + \
    geom_point(alpha = 0.1)
```


We can also add colors for all the points




```python
ggplot(aes(x = 'weight', y = 'hindfoot_length'),data = surveys_complete) + \
    geom_point(alpha = 0.1, color = "blue")
```


Or to color each species in the plot differently:




```python
# ggplot(data = surveys_complete, aes(x = weight, y = hindfoot_length)) +
#    geom_point(alpha = 0.1, aes(color=species_id))

ggplot(aes(x = 'weight', y = 'hindfoot_length', color='species_id'),data = surveys_complete) + \
    geom_point( alpha = 0.1)
```


# Boxplot

Visualising the distribution of weight within each species.



R code:

```R
ggplot(data = surveys_complete, aes(x = species_id, y = hindfoot_length)) +
    geom_boxplot()
```


```python
ggplot( aes(x = 'species_id', y = 'hindfoot_length'), data = surveys_complete) + geom_boxplot()
```


By adding points to boxplot, we can have a better idea of the number of
measurements and of their distribution:



R code:
```R
ggplot(data = surveys_complete, aes(x = species_id, y = hindfoot_length)) +
    geom_jitter(alpha = 0.3, color = "tomato") +
  geom_boxplot(alpha = 0)
```


```python
surveys_complete['species_factor'] = surveys_complete['species_id'].astype('category').cat.codes


xlabels = sorted(set(surveys_complete['species_id'].values) )
xcodes = sorted(set(surveys_complete['species_factor'].values))

ggplot(aes(x = 'species_factor', y = 'hindfoot_length'),data = surveys_complete) + \
    geom_point(position='jitter',alpha=0.7,jittersize=0.4) + \
        scale_x_continuous(breaks=xcodes, labels=xlabels) + \
                         xlab('species_id') + geom_boxplot(alpha=0)

```


Notice how the boxplot layer is behind the jitter layer? What do you need to
change in the code to put the boxplot in front of the points such that it's not
hidden.

## Challenges

> Boxplots are useful summaries, but hide the *shape* of the distribution. For
> example, if there is a bimodal distribution, this would not be observed with a
> boxplot. An alternative to the boxplot is the violin plot (sometimes known as a
> beanplot), where the shape (of the density of points) is drawn.
>
> - Replace the box plot with a violin plot; see `geom_violin()`
>
> In many types of data, it is important to consider the *scale* of the
> observations.  For example, it may be worth changing the scale of the axis to
> better distribute the observations in the space of the plot.  Changing the scale
> of the axes is done similarly to adding/modifying other components (i.e., by
> incrementally adding commands).
>
> - Represent weight on the log10 scale; see `scale_y_log10()`
>
> - Create boxplot for `hindfoot_length`.
>
> - Add color to the datapoints on your boxplot according to the plot from which
>   the sample was taken (`plot_id`)

Hint: Check the class for `plot_id`. Consider changing the class of `plot_id`
from integer to factor. Why does this change how R makes the graph?




```python
## Challenges:
##  Start with the boxplot we created:
ggplot(aes(x = 'species_factor', y = 'hindfoot_length'),data = surveys_complete) + \
    geom_jitter(alpha=0.3) + \
        scale_x_discrete(breaks=xcodes, labels=xlabels) + \
                         xlab('species_id') + geom_boxplot(alpha=0)
```


```python
##  1. Replace the box plot with a violin plot; see `geom_violin()`.

ggplot(aes(x = 'species_factor', y = 'hindfoot_length'),data = surveys_complete) + \
    geom_jitter(alpha=0.3) + \
        scale_x_discrete(breaks=xcodes, labels=xlabels) + \
                         xlab('species_id') + geom_violin(alpha=0)
```


```python
##  2. Represent weight on the log10 scale; see `scale_y_log10()`.
ggplot(aes(x = 'species_factor', y = 'hindfoot_length'),data = surveys_complete) + \
    geom_jitter(alpha=0.3) + \
        scale_x_discrete(breaks=xcodes, labels=xlabels) + \
                         xlab('species_id') + geom_violin(alpha=0) + \
            scale_y_log(base=10)
```


```python
##  3. Create boxplot for `hindfoot_length`.
ggplot(aes(x = 'species_factor', y = 'hindfoot_length'),data = surveys_complete) + \
    geom_jitter(alpha=0.01) + \
        scale_x_discrete(breaks=xcodes, labels=xlabels) + \
                         xlab('species_id') + geom_boxplot(alpha=0) + \
            scale_y_log(base=10)
            
```


```python
##  4. Add color to the datapoints on your boxplot according to the
##  plot from which the sample was taken (`plot_id`).
##  Hint: Check the class for `plot_id`. Consider changing the class
##  of `plot_id` from integer to factor. Why does this change how R
##  makes the graph?

ggplot(aes(x = 'species_factor', y = 'hindfoot_length', color='plot_id'),data = surveys_complete) + \
    geom_jitter(alpha=0.01) + \
        scale_x_discrete(breaks=xcodes, labels=xlabels) + \
                         xlab('species_id') + geom_boxplot(alpha=0) + \
            scale_y_log(base=10)
     
```



# Plotting time series data

Let's calculate number of counts per year for each species. To do that we need
to group data first and count records within each group.




```python
yearly_counts = surveys_complete[['year','species_id']].groupby(['year', 'species_id']).size().reset_index()
yearly_counts.columns = ['year','species_id', 'n']
yearly_counts
```


Timelapse data can be visualised as a line plot with years on x axis and counts
on y axis.




```python
ggplot(aes(x = 'year', y = 'n'),data = yearly_counts) + \
     geom_line()
```


Unfortunately this does not work, because we plot data for all the species
together. We need to tell ggplot to draw a line for each species by modifying
the aesthetic function to include `group = species_id`.




```python
ggplot(aes(x = 'year', y = 'n', group='species_id'),data = yearly_counts) + geom_line()
```


We will be able to distinguish species in the plot if we add colors.




```python
ggplot(aes(x = 'year', y = 'n', color='species_id'),data = yearly_counts) + geom_line()
```


# Faceting

ggplot has a special technique called *faceting* that allows to split one plot
into multiple plots based on a factor included in the dataset. We will use it to
make one plot for a time series for each species.




Now we would like to split line in each plot by sex of each individual
measured. To do that we need to make counts in data frame grouped by year,
species_id, and sex:




```python
yearly_sex_counts = surveys_complete.groupby( ['year','species_id', 'sex']).count()
yearly_sex_counts['n']  = yearly_sex_counts['record_id']
yearly_sex_counts = yearly_sex_counts['n'].reset_index()
yearly_sex_counts
```


We can now make the faceted plot splitting further by sex (within a single plot):




```python
 ggplot(aes(x = "year", y = "n", color = "species_id", group = "sex"), data = yearly_sex_counts, ) + \
     geom_line() + \
         facet_wrap( "species_id")
```


Usually plots with white background look more readable when printed.  We can set
the background to white using the function `theme_bw()`. Additionally you can also remove
the grid.




```python
 ggplot(aes(x = "year", y = "n", color = "species_id", group = "sex"),data = yearly_sex_counts ) + \
     geom_line() + \
            facet_wrap( "species_id") + \
                theme_bw() + \
                theme()
```


To make the plot easier to read, we can color by sex instead of species (species
are already in separate plots, so we don't need to distinguish them further).




```python
ggplot(aes(x = "year", y = "n", color = "sex", group = "sex"), data = yearly_sex_counts) + \
    geom_line() + \
    facet_wrap("species_id") + \
    theme_bw() 
```



# Challenge

> Use what you just learned to create a plot that depicts how the average weight
> of each species changes through the years.

<!-- Answer



```python
yearly_weight = surveys_complete[["year", "species_id","weight"]].groupby(["year", "species_id"]).mean().reset_index()
yearly_weight.columns =   ["year", "species_id","avg_weight"]  
yearly_weight
```


```python
ggplot( aes(x="year", y="avg_weight", color = "species_id", group = "species_id"),data = yearly_weight) + \
    geom_line() + \
    facet_wrap("species_id") + \
    theme_bw()
```


```python
## Plotting time series challenge:
##  Use what you just learned to create a plot that depicts how the
##  average weight of each species changes through the years.

```


The `facet_wrap` geometry extracts plots into an arbitrary number of dimensions
to allow them to cleanly fit on one page. On the other hand, the `facet_grid`
geometry allows you to explicitly specify how you want your plots to be
arranged via formula notation (`rows ~ columns`; a `.` can be used as
a placeholder that indicates only one row or column).

Let's modify the previous plot to compare how the weights of male and females
has changed through time.




```python
## One column, facet by rows
yearly_sex_weight = surveys_complete[
    ['year','sex','species_id','weight']].groupby(
    ["year", "sex", "species_id"]).mean().reset_index()
yearly_sex_weight.columns = ['year','sex','species_id','avg_weight']
yearly_sex_weight
```


```python
ggplot( aes(x="year", y="avg_weight", color = "species_id", group = "species_id"),data = yearly_sex_weight) + \
    geom_line() + \
    facet_grid("sex")
```


```python
# One row, facet by column
ggplot( aes(x="year", y="avg_weight", color = "species_id", group = "species_id"),data = yearly_sex_weight) + \
    geom_line() + \
    facet_grid(None, "sex")
```


# Customization

Take a look at the ggplot2 cheat sheet
(https://www.rstudio.com/wp-content/uploads/2015/08/ggplot2-cheatsheet.pdf), and
think of ways to improve the plot. You can write down some of your ideas as
comments in the Etherpad.

Now, let's change names of axes to something more informative than 'year'
and 'n' and add a title to this figure:




```python
ggplot( aes(x = "year", y = "n", color = "sex", group = "sex"),data = yearly_sex_counts) + \
    geom_line() + \
    facet_wrap( "species_id" ) + \
    labs(title = 'Observed species in time',
         x = 'Year of observation',
         y = 'Number of species') + \
    theme_bw() 
```


The axes have more informative names, but their readability can be improved by
increasing the font size. While we are at it, we'll also change the font family:




```python
ggplot( aes(x = "year", y = "n", color = "sex", group = "sex"),data = yearly_sex_counts) + \
    geom_line() + \
    facet_wrap( "species_id" ) + \
    theme_bw() + \
    theme(axis_title_x = element_text(size=16, family="Arial"),
         axis_title_y = element_text(size=16, family="Arial")) + \
    labs(title = 'Observed species in time',
        x = 'Year of observation',
        y = 'Number of species')
```


After our manipulations we notice that the values on the x-axis are still not
properly readable. Let's change the orientation of the labels and adjust them
vertically and horizontally so they don't overlap. You can use a 90 degree
angle, or experiment to find the appropriate angle for diagonally oriented
labels.




```python
ggplot( aes(x = "year", y = "n", color = "sex", group = "sex"),data = yearly_sex_counts) + \
    geom_line() + \
    facet_wrap( "species_id" ) + \
    labs(title = 'Observed species in time',
        x = 'Year of observation',
        y = 'Number of species') + \
    theme_bw() + \
    theme(axis_text_x = element_text(color="grey", size=10, angle=90, hjust=.5, vjust=.5),
          axis_text_y = element_text(color="grey", size=10, hjust=0),
         ) 
```


If you like the changes you created to the default theme, you can save them as
an object to easily apply them to other plots you may create:





```python
arial_grey_theme = theme(axis_text_x = element_text(color="grey", size=10, angle=90, hjust=.5, vjust=.5),
                          axis_text_y = element_text(color="grey", size=10))
ggplot(surveys_complete, aes(x = 'species_id', y = 'hindfoot_length')) + \
    geom_boxplot() + \
    arial_grey_theme
```


With all of this information in hand, please take another five minutes to either
improve one of the plots generated in this exercise or create a beautiful graph
of your own. Use the RStudio ggplot2 cheat sheet, which we linked earlier for
inspiration.

Here are some ideas:

* See if you can change thickness of the lines.
* Can you find a way to change the name of the legend? What about its labels?
* Use a different color palette (see http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/)

After creating your plot, you can save it to a file in your favourite format.
You can easily change the dimension (and its resolution) of your plot by
adjusting the appropriate arguments (`width`, `height` and `dpi`):




```python
my_plot =  ggplot(yearly_sex_counts, aes(x = "year", y = "n", color = "sex", group = "sex")) 
my_plot += geom_line() 
my_plot += facet_wrap("species_id") 
my_plot += labs(title = 'Observed species in time',
                x = 'Year of observation',
                y = 'Number of species') 
my_plot += theme_bw() 
my_plot += theme(axis_text_x = element_text(color="grey", size=10, angle=90, hjust=.5, vjust=.5),
                        axis_text_y = element_text(color="grey", size=10))
my_plot.save("name_of_file.png", width=15, height=10)
```


```python
## Final plotting challenge:
##  With all of this information in hand, please take another five
##  minutes to either improve one of the plots generated in this
##  exercise or create a beautiful graph of your own. Use the RStudio
##  ggplot2 cheat sheet for inspiration:
##  https://www.rstudio.com/wp-content/uploads/2015/08/ggplot2-cheatsheet.pdf

```
