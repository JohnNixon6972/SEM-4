# Write a Pandas program to create a  Data Frame from csv and perform the followingoperations:
# a)Display column names of data frame
# b)Read the column name and display unique values,
# c)Display frequency of occurrence of each unique value.
# d) Count of total number of records in the Data frame.

import pandas as pd
import numpy as np


df = pd.read_csv("mtcars.csv",index_col=0)
print("Column names :: ")
print(*df.columns,sep=",")
print()

col_name = input("Enter the column name :: ")
if col_name in df.columns:
    uniq = np.unique(df[col_name])
    print(f"Unique Values in column {col_name} are :: ")
    print(*uniq,sep=",")
    print()

    data = list(df[col_name])
    print(f"Frequency of occurances of each unique value in {col_name} column are :: ")
    print("val : count")
    for val in uniq:
        print(val," : ",data.count(val))

else:
    print("Invalid Column-name !!")
print()

print("Number of records in data frame are :: ",df.shape[0])

    

