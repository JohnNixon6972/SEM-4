import csv
import pandas as pd

headers = ["W","X","Y","Z"]
data = [[68,78,84,86],[75,85,94,97],[86,96,89,96],[80,80,83,72],[66,86,86,83]]

with open("dataframe.csv",'w') as fileobj:
    writer = csv.writer(fileobj)

    writer.writerow(headers)
    writer.writerows(data)  

df = pd.read_csv("dataframe.csv")

columns = df.columns
rev_columns = columns[::-1]
print("Orginal order :: ")
print(df[columns])
print()
print("Reversed column Order ::")
print(df[rev_columns])
print()
print("Reverse row order ::")
print(df[::-1])
print()
print("Reverse row order and reset index ::")
print(df[::-1].reset_index(drop = True))