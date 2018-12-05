---   
layout: page                                                                                            
title: "Extra Challenges"                                                                           
permalink: /extra_challenges/                                                                            
---                                                                                                     

# Extra Challenges

A collection of challenges that have been either removed from or not (yet) added to the main lesson. 

> ## Looping Over DataFrame
>
> (Please refer to lesson `06-loops-and-functions.md`)
>
> The file `surveys.csv` in the `data` folder contains 25 years of data from surveys,
> starting from 1977. We can extract data corresponding to each year in this DataFrame
> to individual CSV files, by using a `for` loop:
> 
> ~~~
> import pandas as pd
> 
> # Load the data into a DataFrame
> surveys_df = pd.read_csv('data/surveys.csv')
> 
> # Loop through a sequence of years and export selected data
> start_year = 1977
> end_year = 2002
> for year in range(start_year, end_year+1):
>
>     # Select data for the year
>     surveys_year = surveys_df[surveys_df.year == year]  
>
>     # Write the new DataFrame to a CSV file
>     filename = 'data/surveys' + str(year) + '.csv' 
>     surveys_year.to_csv(filename)
> ~~~
> {: .language-python}
>
> What happens if there is no data for a year in a sequence? For example,
> imagine we used `1976` as the `start_year`
>
> > ## Solution
> > We get the expected files for all years between 1977 and 2002,
> > plus an empty `data/surveys1976.csv` file with only the headers.  
> {: .solution}  
{: .challenge}
