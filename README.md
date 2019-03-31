# NYC Subway Dataset Analysis

This project aims to decide whether more people ride NYC subway when it is raining or when it is not raining.

## Statistical Test

Mann–Whitney U test, using two-tail P value is used to analyze the NYC subway data.

**Null hypothesis**: there is no significant difference between the average ridership in rainy & non-rainy hours.

**P-critical value**: 0.05

###Results

- U = 1924409167.0
- P-value = 0.024*2=0.048
- Mean of ridership with rain = 1105
- Mean of ridership without rain = 1090

So I can reject null hypothesis, as p-value is less than p-critical value, and assure that there is a significant difference between the average ridership in rainy and non-rainy hours.

## Linear Regression

In my regression model, Gradient descent is used to compute the coefficients theta and produce prediction for ENTRIESn_hourly with some modifications on the feature list and the dummy variable, the result r squared was 0.50.

After plotting the residual between the resulted predictions and the observed ones as shown on figure 2, I found that it has a normal distribution which is a good indicator of using the regression model, but I was interested to use another approach of the linear regression. So I decided to use OLS using Statsmodels.

**Model Features**

- Features: rain, meantempi
- Dummy variables: Hour, UNIT

**Features Coefficients**

- rain: 2.88
- meantempi: -8.04

**Model R_Squared value: 0.5**

The resulted R_Squared value indicates that the model (with its features) accounts for 50 % of the variability of the ridership.I think that this linear model to predict ridership is appropriate for this dataset because this value of r squared means that there is a linear relationship exists between features and the ridership.

## Conclusion

Using Mann–Whitney U test, with two-tail P value indicated that there is a significant difference between the average ridership on rainy and non-rainy hours, because the p-value (0.048) is less that 0.05.

The results shows that there is a difference of 15 entries increase in the mean ridership in rainy hours than non-rainy hours.

Using my regression model OLS, I expect that the ridership is increased by 2.88 when it is raining if the other features are fixed.
