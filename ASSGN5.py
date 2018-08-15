# Q.1 - Download the dataset from this link and solve all these questions, 
Click Here
a.) Find the sum of missing data for every column in the dataset using the
(isnull function and sum function) 
b.) Remove the missing values (if any) 
c.) Once again , Import the dataset and this time replace the missing null
values with mean of the column series. 
d.) Find individual data types and copy the temperature column to a pandas
series.

import pandas as pd
file = pd.read_csv("weather.csv")
print("data frame is-")
file
print(" Finding the sum of missing data for every column in the dataset-")
file.isnull().sum()
print("Remove the missing values-")
file.dropna()
print("Replacing null values with mean- ")
file.fillna(file.mean())
print("Finding individual data types-")
file.dtypes
print("copying the  minimum temperature column to a pandas series-")
var=file.MinTemp
pd.Series(var)
