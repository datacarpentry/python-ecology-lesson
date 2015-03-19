# Matplotlib

## About Matplotlib

[Matplotlib](http://matplotlib.org/) is a library that can be used to visualize data that has been loaded with a library like Pandas, Numpy, or Scipy. For this tutorial, we'll use Pandas.

## Loading Data

For a more detailed tutorial on loading data, see [this lesson on .beginning with Pandas](https://github.com/datacarpentry/datacarpentry/blob/master/lessons/python/01-starting-with-data.md)

For now, we'll just use a simple statement to load the surveys data.

```python
import pandas as pd
df = pd.read_csv('data/surveys.csv', index_col='record_id')
```

Matplotlib has a wide variety of plots that it can produce. First, we'll introduce the simplest of plots: the 2 dimensional line plot.

First, we'll import matplotlib.

```python
import matplotlib.pyplot as plt
```

Matplotlib can easily plot a set of data even larger than `surveys.csv`, but for this example, we'll take the first 50 of the ~35000 entries that are in `surveys.csv.` For a more detailed tutorial on slicing data, see [this lesson on masking and grouping](https://github.com/datacarpentry/datacarpentry/blob/master/lessons/python/05-masking-and-groups.md).

```python
small_dataset = df[:50]
```

There's a column in `surveys.csv` named "plot" which would make an excellent value to plot.

```python
plot_data = small_dataset['plot']
```

## Simple Plotting

Now, we have an array of plot data indexed by the `record_id` value. Let's plot it and give it a label.

```python
plt.plot(plot_data, label='My Data')
```

The data has now been plotted, to see it we can do 2 things:

1. We can interact with the plot by using `plt.show` like so:

```python
plt.show()
```

2. Or we can save the plot to a file using `plt.savefig` like so:

```python
plt.savefig('myplot.png')
```

This would save the file as a rasterized PNG image. The format is deduced from the file name or can be given explicitly using `format` parameter, eg. `format="png"`. For raster images, in order to enhance quality one can also request particulat resolution in dots per inch using `dpi` parameter. This may be useful when creating quality images for printing/publication. Vectorized images are supported as well, we just need to save the file as a SVG, EPS or PDF which is as simple as:

```python
plt.savefig('myplot.pdf')
```

## Plot Essentials

What's a plot without a title, axis labels, and a legend? These can be easily set like so:

```python
plt.xlabel('Index')
plt.ylabel('Plot Value')
plt.title('The Plot Value From surveys.csv')
```

## Clearing the Plot

The plot is created using some default settings, eg. default line color. You may have noticed, the first line plotted is blue.  We can change this by replotting the figure. But first, the blue line is still on the plot, so we must clear it like so:

```python
plt.clf()
```

## Managing figures

It is important to note, that subsequent plots we may have created with `plt.plot` are (by default) superimposed on the same figure that is created implicitly upon first `plt.plot` call. Figures are numbered from 1 and one can switch between them by calling `plt.figure(number)`. When creating a new figures one can give a number of options, for example one can fine tune the size and default resolution by using `figsize` and `dpi` parameters:

```python
plt.figure(figsize=(10, 8), dpi=200)
```

which will create a figure 8 inches high and 10 inches wide with resolution of 200 dots per inch.

It is also possible to control the margin between the edge of the axes box and the edge of the image:

```python
plt. subplots_adjust(left=0.1, bottom=0.2, right=0.99, top=0.99)
```

Values are fractions of the image size and denote the position of the respective edge of the axes bounding box. Lower left corner of the image is at (0,0). The invocation above leaves 10% margin on the left side, 20% margin on the bottom and 1% for top and right edges.

## Managing styles

### Colors

To use a different color, like red, we would plot our data like so:

```python
plt.plot(plot_data, color='r')
```

Note that creating more than one plot on the same figure will make them use different colors (like in gnuplot) unless specified otherwise. Here's a list of predefined colors:

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

or use RGB coefficients of range 0-1 (which makes it easy to create multiple color-encoded plots in a loop):

```
plt.plot(plot_data, color=(0.1, 0.9, 0.6))
```

### Line style

The default line style is a solid line. We can make it thinner or thicker by specifying `linewidth` or `lw`:

```python
plt.plot(plot_data, linewidth=3)
```

The default linewidth is 1. A linewidth of 3 would be 3 times as thick as the default. Likewise, a linewidth of .75 would be 3/4 of the thickness of the default.



## Other types of plots

Matplotlib can do many types of plots. For example, a dot plot can be constructed like so:

```python
plt.plot(plot_data, 'o')
```

The `o` means a dot. There are a variety of markers you can use. Here's a complete list: http://matplotlib.org/api/markers_api.html#module-matplotlib.markers

A simple bar plot:

```
plt.plot(plot_data, linestyle='--')
```

Value | Style
----- | -----
'-'|solid line (default)
'--'|dashed line
'-.'|dash-dot line
':' |dotted line

### Marker style

So far we have plotted only a simple line plot which is default. It is possible to specify also the data marker style which will create scatter plot or various connect-the-dots-like plot. For example, to use square data marker:

```
plt.plot(plot_data, marker='s')
```

Marker | Meaning
------ | -------
'.'|point
'o'|circle
'v'|triangle down
'^'|triangle up
's'|square
'p'|pentagon
'*'|star
'h'|hexagon
'+'|plus
'D'|diamond

## Configuration of plot axes

So far we have used a simple, default, uniform axis. The user has, however, a complete control over the way axes are organized.

## Plot range

One can adjust the range of axes using set `plt.xlim` for horizontal and `plt.ylim` for vertical axis. For instence to set X limt to [-10; 15] one can use:

```
plt.xlim(-10, 15)
```

### Plot scale

In many cases it is useful to use logarithmic scale on one or both axes. One can use dedicated plot methods:

Method | Result
------ | ------
`plt.semilogx`|logarithmic scaling on X-axis
`plt.semilogy`|logarithmic scaling on Y-axis
`plt.loglog`|logarithmic scaling on both axes (log-log plot)

```python
plt.loglog(plot_data)
```

### Two independent X or Y axes

To create a plot with two X or two Y axes having different scales, units, ranges one can use `plt.twinx` and `plt.twiny`:


```python
plt.bar(plot_data.index, plot_data.values)
plt.twinx()
plt.plot(1/ plot_data, color='k')
```

This will create a plot with two independent Y axes, one for barplot and one for line plot of inverse values. Both plots will share the same X-axis.

## Describing the plot

In the examples above the plot is not ready to be published. We would like to add titles, axes labels, tick markers, maybe some grid or legend.

### Adding legend

All plots can be labelled upon creation:

```python
plt.plot(..., label='some description')
```

and a legend can be automatically generated in the automatically chosen _best_ location:

```python
plt.legend(loc='best')
```

### Modifying ticks

One can change the location and labels of the axes ticks using `plt.xticks` and `plt.yticks` methods:

```python
`plt.xticks([1,2,3,4])` # put ticks in given locations of X-axis

`plt.yticks([1,2,3], ['A', 'B', 'C'])` # put ticks in given locations on Y-axis, denote them with letters
```

Labels can be rotated by adding parameter `rotation=angle_in_degrees`. To draw a grid with grid lines at the ticks use `plt.grid()`.

### Labelling

Axes can be labelled using:

```python
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
```

To set a title use

```python
plt.title('Plot title')
```

## Plot variations

Matplotlib supports a number of different plot variations, eg. bar plot (`plt.bar`), contour plots (`plt.contour`), pie chart (`plt.pie`), error bars (`plt.errorbar`), polar plot (`plt.polar`), ...

To use a bar plot:

```python
plt.bar(plot_data.index, plot_data.values)
```

# Go exploring

There are excellent examples on [Matplotlib](http://matplotlib.org/) website, especially:

* [Matplotlib Gallery](http://matplotlib.org/gallery.html) 
* [Scipy Cookbook](http://wiki.scipy.org/Cookbook/Matplotlib)

A box and whisker plot:

```python
plt.boxplot(plot_data.values)
```

# A Realistic Example

You may have noticed there's some more data beyond just the plot value in `surveys.csv`. Let's plot the plot value and group them by the sex value. A dot plot would be ideal for this.

Pandas has some built-in tools that make it easy to group your data.

```python
grouped_plot_data = small_dataset.groupby('sex')
```

This returns our data in an iterable object. Each entry in `grouped_plot_data` is formatted like so:

```python
('group_name', pandas data pertaining to the group)
```

Keep in mind we need different colors and labels for each group. So we can plot the data like so:

```python
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

## More Information

This is a basic tutorial to get you started using Python to make your graphs. For more information on Matplotlib, visit the official site: http://matplotlib.org/

