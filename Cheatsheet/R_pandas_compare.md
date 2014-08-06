##Useful links (essentially what I used to help make this chart) 

[Climate Ecology R and Pandas comparison](http://climateecology.wordpress.com/2014/02/10/a-side-by-side-example-of-r-and-python/)  

[Pandas reference material](http://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html)  

[Yhat, the makers of Python ggplot, have an R and Pandas comparison](http://blog.yhathq.com/posts/R-and-pandas-and-what-ive-learned-about-each.html) 


**What is R?** R is a general-purpose statistical programming environment. Similar to many programming languages, it has different packages that users have contributed for use with specific functions. R has many packages for analysis and visualization that can be called upon for functions. 

**What is Pandas?** Pandas is a statistical programming library. Like R, Python has many packages contributed by users for specific functions. Pandas is one such library. It is meant to interoperate with different libraries for analysis and visualization.
To use these R functions, simply start R. To use pandas functions, open a Python interpreter and type:

```python
import pandas as pd
import numpy
```

For information on reading data into R, see [here](https://github.com/datacarpentry/datacarpentry/blob/master/lessons/R/01-starting-with-data.Rmd) and for the same in Pandas, see [here](https://github.com/datacarpentry/datacarpentry/blob/master/lessons/python/01-starting-with-data.md).

| 		| R 									| Pandas |
|-------|---------------------------------------|--------|
|**General**| large library of statistical functions | Stand-alone library, Python being the equivalent of ‘R’ on the whole 
|       | large user community (been around longer) | relatively young, but readably documented, module | 
|		| RStudio is good IDE, not many others | Many IDEs available |
|-------|--------------------------------------|----------|
|**Data Structures**| array | list |
|       | lists | dictionary |
|       | data.frame | dataframe |
|-------|-----------------|------------------------|
|**Read Data (.csv file)**| df<-read.csv(“myfile.csv”) | df=pd.read_csv(“blah.csv”) |
|-------|------------------|-------------------|
| **Clean Up** | **drop incomplete data**            | **drop incomplete data** |
|		|	  weight<-subset(df,weight!=’NA’) | weight=df.dropna(subset=[‘weight’]) |
|       |  **fixing data errors**              |   **fixing data errors** |
|       |   df$temp[which(df$temp==45)]<-42   | df[‘temp’’].replace(45, 42, inplace=True) |
|-------|--------------------------------------|-------------------------------------------|
|**Slicing** | **access columns by name** | **access columns by name**\s\s |
|        |df[ , c( “a”, “b”, “c”)] | df[[“a”, “b”, “c”]] |
|        |                         | or |
|        |                         | df.loc[ : , [“a”, “b”, “c”]] |
|        | **access columns by location** |   **select multiple, noncontinguous, columns by location--use .iloc and numpy.r** |
|        | df[, c(1:10, 35:40)]         |      df.iloc[ : , np.r_[:10, 35:40]] |
|--------|------------------------------|--------------------------------------|
|**Match** | **select data using %in%, which   | **return vector of match positions** |
|      | returns logical vector indicating | g.isin([2,4]) |
|      |  if there is a match or not** |     **apply() method to return a pandas series of matches** |
|      |   g %in% c(1,10)       |     pd.Series(pd.match(g,[1,10], np.nan)  |
|      | **return vector of match positions** |   |
|		| match( g, c(1,10)) | |
|-------|-------------------|------------------|
|**Subset** | **get rows of dataframe that satisfy some statement** | get rows of dataframe that satisfy some statement** |
|       | subset(df, weight <= 100) | **query() method** |
|       |                           | df. query(“weight” <= 100) |
|       | **fancy subsetting with matching**       | **standard slicing** |
|       | spec<-c(“elephant”, “giraffe”,“ostrich”)  | df[df.weight <= 100] |
|       |  sub_dat<-[df$species %in% species, ] | **boolean indexing** | 
|		|							            | df.loc[df.weight <=100] |
|		|										| **fancy subsetting with matching** |
|		|										| spec=[“elephant”, “giraffe”, “ostrich”] |
|		|	    								| sub_dat=df[species[‘species’].isin(spec)] |
|-----|-----------------------------|-------------------------------------------|
|**Aggregate** | **aggregate function to split data and compute means for each** |  **grouby() method** |
|              |aggregate(x=df[, c("v1", "v2")], by=list(mydf2$by1,mydf2$by2),FUN=mean) | g=df.grouby([“by1”, “by2”]) |
|		       |**tapply is similar to aggregate but can be used on ragged arrays** | g[[“v1”, “v2”]].mean()   |
|              |tapply(animals$avg_wgt,animals$sex, mean)  | **pivot_table() method is pandas equivalent of tapply** |
|		                                       |    animals.pivot_table(values=”weight”, columns=”sex”, aggfunc=np.mean) |	|--------------|--------------------------------------|---------------------|
|**Apply functions** | **with() method**              | **eval() method**  |
|       |  with(df, x+y)                        | df.eval(“x+y”)   |
|       | apply, sapply, lapply                 | apply            |
|------------------------|-----------------------------------------|
|**Split-Apply Combine** | plyr package--ddply allows you to summarize data | groupby allows transformations, aggregations,  |  |       |                                       | and easy-access plotting functions |
|**Reshape** | **reshape2 package to switch data between wide and long formats** | **stacking and unstacking with melt and  		|	melt.array to melt array into data frame | pivot methods**  |
|       | data.frame(melt(a))					| DataFrame([tuple(list(x)+[val]) for x, val in np.ndenumerate(a)]
|       | melt.list to melt list into dataframe | Dataframe method |
|       | data.frame(melt(a))                   | DataFrame(a) | 
|       | **melt.data.frame to reshape dataframe** | **melt method** |
|       | melt(df, id=(“a”, “b”))               | pd.melt(df, id_vars=[“a”, “b”]) |
|**Plotting**| plot, hist, boxplot                  | matplotlib    |
|        | ggplot2 package						| ggplot2 package |
|        |                                      | native pandas (hist, plot, boxplot) |

   


