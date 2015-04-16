'''
Jelly Bean Code
========

The Jelly Bean Code was originally created as a Software Carpentry
Instructor final project by Rachel Slaybaugh of UC Berkeley.

https://github.com/rachelslaybaugh/JellyBeanCode
'''

# This script estimates the number of jelly beans in the world using input data determined to be correlated to this result.

#The number of jelly beans in the world is correlated to the fraction of land used for sugar, the world population, and the fraction of people who like the color pink.


# Set the fraction of land being used for sugar, the world population,
# and the fraction of the population that loves pink.

fracLand4Sugar = 0.1        # Fraction of land used for growing sugar
worldPop = 7e9              # World population
scalingConst = 1e-1         # Scaling constant used in estimate
fracPplLovingPink = 0.18    # Fraction of people who love the color pink.

''' TO DO:
(1) Write assertions to check that the input values are reasonable (can fracLand4Sugar be negative? what's the highest value it could be? ...)
(2) Make sure the values are the correct type (can they be strings? integers?)
(3) Write an assertion to check that all of the needed values have been defined
'''

# Get the estimate of the number of jelly beans in the world,
# and report the result given the input.
est = fracLand4Sugar * worldPop * scalingConst / (1.0 - fracPplLovingPink)
''' TO DO:
(4) Write this equation into a function
'''


print "\nIt is estimated that when\n", fracLand4Sugar*100, "percent\nof the land is used for sugar and\n", fracPplLovingPink*100, "percent of", worldPop, "people\nLOVE pink, then there are\n", est, "\nJelly Beans in the world."



''' TO DO:
(5) Write a script that creates a three plot figure:
    (Subplot 1) Number of jelly beans against population size
    (Subplot 2) Number of jelly beans against fraction of land used for sugar
    (Subplot 3) Number of jelly beans against fraction of pink lovers

Hint: You can create a one-dimensional numpy array of equally spaced values with:
import numpy as np
array_name = np.arange(start_value, end_value, step_size)
'''
