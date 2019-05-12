# NYC Subway Dataset Analysis

This project is a part of the [Data Analyst Nanodegree](https://www.udacity.com/course/data-analyst-nanodegree--nd002) at [Udacity](https://www.udacity.com/)

-- Project Status: Completed

## Project Introduction

Analyzing NYC Subway Dataset to decide whether more people ride NYC subway when it is raining or when it is not raining.

## Methods Used

- Statistical Test
- Linear Regression
- Data Visualization

## Technologies

- Python 2.7
- Numpy
- Pandas
- Scipy
- Statsmodels
- Matplotlib

## Project Description

The goal of the project is to detect any significant difference between the average ridership in rainy & non-rainy hours and quantify it if exists.
First, I used Mann–Whitney U test that revealed a significant difference between the average ridership in rainy & non-rainy hours. Then, I developed a linear regression model that expected the ridership to be increased by 2.88 when it is raining if the other features are fixed. (for more details of the analysis process see this [document](https://github.com/eng-dtarek/NYC_Subway_Data_Analysis/blob/master/Analyzing%20the%20NYC%20Subway%20Dataset.pdf)).

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/en/articles/cloning-a-repository)).
2. Install the above technologies.
3. Each folder handles part of the analysis process. for example "mann_whitney_u_test" applies a statistical test on the dataset and returns the mean number of entries with rain, the mean number of entries without rain, and the Mann-Whitney U statistic and p-value >> cd mann_whitney_u_test >> python mann_whitney_u.py

## References

- [https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/](https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/)
- [https://flowingdata.com/2014/02/27/how-to-read-histograms-and-use-them-in-r/](https://flowingdata.com/2014/02/27/how-to-read-histograms-and-use-them-in-r/)
- [https://help.plot.ly/make-a-histogram/](https://help.plot.ly/make-a-histogram/)
- [https://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm](https://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm)
- [https://en.wikipedia.org/wiki/Ordinary_least_squares](https://en.wikipedia.org/wiki/Ordinary_least_squares)
- [https://ggplot2.tidyverse.org/reference/geom_bar.html](https://ggplot2.tidyverse.org/reference/geom_bar.html)
- [https://dss.princeton.edu/online_help/analysis/interpreting_regression.htm](https://dss.princeton.edu/online_help/analysis/interpreting_regression.htm)
- [http://people.duke.edu/~rnau/regintro.htm](http://people.duke.edu/~rnau/regintro.htm)
- [https://stats.idre.ucla.edu/](https://stats.idre.ucla.edu/)
- [https://www.graphpad.com/guides/prism/6/statistics/index.htm?one-tail_vs__two-tail_p_values.htm](https://www.graphpad.com/guides/prism/6/statistics/index.htm?one-tail_vs__two-tail_p_values.htm)

