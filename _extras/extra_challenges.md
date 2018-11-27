---   
layout: page                                                                                            
title: "Extra Challenges"                                                                           
permalink: /extra_challenges/                                                                            
---                                                                                                     

# Extra Challenges

A collection of challenges that have been either removed from or not (yet) added to the main lesson. 

> ## Looping Over Dataframe
>
> (Please refer to lesson `06-loops-and-functions.md`)
>
> The file `surveys.csv` in the `data` folder contains 25 years of data from surveys,
> starting from 1977. We can load the data and print all the years surveyed using a `for` loop:
> 
> ~~~
> import pandas as pd
> 
> # Load the data into a DataFrame
> surveys_df = pd.read_csv('data/surveys.csv')
> 
> # Loop through a sequence of years and print the year
> start_year = 1977
> end_year = 2002
> for year in range(start_year, end_year+1):
>     print(str(year))
> ~~~
> {: .language-python}
>
> What happens if there is no data for a year in a sequence? For example,
> imagine we used `1976` as the start year in `range`
>
> > ## Solution
> > An empty file with only the headers  
> {: .solution}  
{: .challenge}
