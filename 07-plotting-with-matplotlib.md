# About Matplotlib

Matplotlib is a library that can be used to visualize data that has been loaded with a library like Pandas, Numpy, or Scipy. For this tutorial, we'll use Pandas.

# Loading Data

For a more detailed tutorial on loading data, see (insert link here). For now, we'll just use a simple statement to load the surveys data.

```
import pandas as pd
df = pd.load_csv('data/surveys.csv', index_col='record_id')
```

Matplotlib has a wide variety of plots that it can produce. First, we'll introduce the simplest of plots: the 2 dimensional line plot.

First, we'll import matplotlib.

```
import matplotlib.pyplot as plt
```

Matplotlib can easily plot a set of data even larger than `surveys.csv`, but for this example, we'll take the first 50 of the ~35000 entries that are in `surveys.csv.` For a more detailed tutorial on slicing data, see (insert link here).

```
small_dataset = df[:50]
```

There's a column in `surveys.csv` named "plot" which would make an excellent value to plot.

```
plot_data = small_dataset['plot']
```

# Simple Plotting

Now, we have an array of plot data indexed by the `record_id` value. Let's plot it.

```
plt.plot(plot_data)
```

The data has now been plotted, to see it we can do 2 things:

1. We can interact with the plot by using `plt.show` like so:

```
plt.show()
```

2. Or we can save the plot to a file using `plt.savefig` like so:

```
plt.savefig('myplot.png')
```

This would save the file as a rasterized png. But if we wanted a vectorized image, we just need to save the file as a pdf:

```
plt.savefig('myplot.pdf')
```

# Clearing the Plot

The default color, you may have noticed, is blue. We can change this by plotting again. But first, the blue line is still on the plot, so we must clear it like so:

```
plt.clf()
```

# Colors

To use a different color, like red, we would plot our data like so:

```
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

```
plt.plot(plot_data, color='#aa5599')
```

# Line Styles

The default line style is a solid line. We can make it thinner or thicker by specifying linewidth:

```
plt.plot(plot_data, linewidth=3)
```

The default linewidth is 1. A linewidth of 3 would be 3 times as thick as the default. Likewise, a linewidth of .75 would be 3/4 of the thickness of the default.

# Other Plots

To use a bar plot:

```
plt.bar(plot_data.index, plot_data.values)
```

