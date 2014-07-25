# Matplotlib

## About Matplotlib

[Matplotlib](http://matplotlib.org/) is a library that can be used to visualize data that has been loaded with a library like Pandas, Numpy, or Scipy. For this tutorial, we'll use Pandas.

## Loading Data

For a more detailed tutorial on loading data, see https://github.com/datacarpentry/datacarpentry/blob/master/lessons/python/01-starting-with-data.md

For now, we'll just use a simple statement to load the surveys data.

```python
import pandas as pd
df = pd.load_csv('data/surveys.csv', index_col='record_id')
```

Matplotlib has a wide variety of plots that it can produce. First, we'll introduce the simplest of plots: the 2 dimensional line plot.

First, we'll import matplotlib.

```python
import matplotlib.pyplot as plt
```

Matplotlib can easily plot a set of data even larger than `surveys.csv`, but for this example, we'll take the first 50 of the ~35000 entries that are in `surveys.csv.` For a more detailed tutorial on slicing data, see https://github.com/datacarpentry/datacarpentry/blob/master/lessons/python/05-masking-and-groups.md

```python
small_dataset = df[:50]
```

There's a column in `surveys.csv` named "plot" which would make an excellent value to plot.

```python
plot_data = small_dataset['plot']
```

## Simple Plotting

Now, we have an array of plot data indexed by the `record_id` value. Let's plot it and give it a label.

``python
plt.plot(plot_data, label='My Data')
```

The data has now been plotted, to see it we can do 2 things:

1. We can interact with the plot by using `plt.show` like so:

```python
plt.show()
```

![Example of bar plot](pics/myplot.png)

2. Or we can save the plot to a file using `plt.savefig` like so:

```python
plt.savefig('myplot.png')
```

This would save the file as a rasterized png. But if we wanted a vectorized image, we just need to save the file as a pdf:

```python
plt.savefig('myplot.pdf')
```

# Plot Essentials

What's a plot without a title, axis labels, and a legend? These can be easily set like so:

```
plt.xlabel('Index')
plt.ylabel('Plot Value')
plt.title('The Plot Value From surveys.csv')
```

# Clearing the Plot

The default color, you may have noticed, is blue. We can change this by plotting again. But first, the blue line is still on the plot, so we must clear it like so:

```python
plt.clf()
```

### Colors

To use a different color, like red, we would plot our data like so:

```python
plt.plot(plot_data, color='r')
```

Here's a list of predefined colors:

Code | Color
---- | -----
b | blue
g | green
r | red
c | cyan
m | magenta
y | yellow
k | black
w | white

For more color flexibility, you can specify hexadecimal RGB values like so:

```python
plt.plot(plot_data, color='#aa5599')
```

### Line Styles

The default line style is a solid line. We can make it thinner or thicker by specifying linewidth:

```python
plt.plot(plot_data, linewidth=3)
```

The default linewidth is 1. A linewidth of 3 would be 3 times as thick as the default. Likewise, a linewidth of .75 would be 3/4 of the thickness of the default.

## Other Plots

A dot plot:

```
plt.plot(plot_data, 'o')
```

The `o` means a dot. There are a variety of markers you can use. Here's a complete list: http://matplotlib.org/api/markers_api.html#module-matplotlib.markers

A simple bar plot:

```python
plt.bar(plot_data.index, plot_data.values)
```
![Example of bar plot](pics/barplot.png)

## Go exploring

There are excellent examples on [Matplotlib](http://matplotlib.org/) website, especially:

* [Matplotlib Gallery](http://matplotlib.org/gallery.html)
* [Scipy Cookbook](http://wiki.scipy.org/Cookbook/Matplotlib)
=======
A box and whisker plot:

```
plt.boxplot(plot_data.values)
```

# A Realistic Example

You may have noticed there's some more data beyond just the plot value in `surveys.csv`. Let's plot the plot value and group them by the sex value. A dot plot would be ideal for this.

Pandas has some built-in tools that make it easy to group your data.

```
grouped_plot_data = small_dataset.groupby('sex')
```

This returns our data in an iterable object. Each entry in `grouped_plot_data` is formatted like so:

```
('group_name', pandas data pertaining to the group)
```

Keep in mind we need different colors and labels for each group. So we can plot the data like so:

```
colors = ['r', 'g'] #we'll be cycling through these colors
color_index = 0
for group in grouped_plot_data:
    color = colors[color_index]
    group_label = group[0]
    group_data = group[1]
    plt.plot(group_data['plot'], color=color, label=group_label)
    color_index += 1
plt.legend()
```

# More Information

This is a basic tutorial to get you started using Python to make your graphs. For more information on Matplotlib, visit the official site: http://matplotlib.org/

