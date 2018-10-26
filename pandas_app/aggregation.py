import pandas as pd
import numpy as np

# 聚合函数

df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2020', periods=10),
                  columns=['A', 'B', 'C', 'D'])
print("df:")
print(df)
print()

r = df.rolling(window=3, min_periods=2)
print("rolling:", r)
print()

# DataFrame aggregate
print("DataFrame aggregate:")
print(r.aggregate(np.sum))
print()

# Series aggregate
print("Series aggregate:")
print(r['A'].aggregate(np.sum))
print()

# multi Series aggregate
print("multi Series aggregate:")
print(r[['A', 'B']].aggregate(np.sum))
print()

# multi Series aggregate 2
print("multi Series aggregate 2:")
print(r['A', 'B'].aggregate([np.sum, np.mean]))
print()

# multi Series aggregate 3
print("multi Series aggregate 3:")
print(r.aggregate({'A': np.sum, 'B': np.mean}))
print()
