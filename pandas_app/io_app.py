import pandas as pd
import numpy as np

# io函数

df = pd.read_csv("temp.csv")
print("read_csv:")
print(df)
print()

df = pd.read_csv("temp.csv", index_col=['S.No'])
print("read_csv 2:")
print(df)
print()

df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print("read_csv 3:")
print(df.dtypes)
print()

df = pd.read_csv("temp.csv", names=['a', 'b', 'c', 'd', 'e'])
print("read_csv 4:")
print(df)
print()

df = pd.read_csv("temp.csv", names=['a', 'b', 'c', 'd', 'e'], header=0)
print("read_csv 5:")
print(df)
print()

df = pd.read_csv("temp.csv", skiprows=2)
print("read_csv 6:")
print(df)
print()
