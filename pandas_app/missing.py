import pandas as pd
import numpy as np

# 数据丢失函数

df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
print("df:")
print(df)
print()

# DataFrame reindex
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
print("DataFrame reindex:")
print(df)
print()

# DataFrame isnull
print("DataFrame isnull:")
print(df['one'].isnull())
print()

# DataFrame notnull
print("DataFrame notnull:")
print(df['one'].notnull())
print()

# DataFrame sum
print("DataFrame sum:")
print(np.array(df['one']), ':', df['one'].sum())
print()

# DataFrame sum
df1 = pd.DataFrame(index=[0, 1, 2, 3, 4, 5], columns=['one', 'two'])
print(df1)
print("DataFrame sum:")
print(np.array(df1['one']), ':', df1['one'].sum())

# DataFrame NaN replaced with '0'
print("NaN replaced with '0':")
print(df.fillna(0))
print()

# DataFrame NaN dropna
print("NaN dropna:")
print(df.dropna())
print()

df2 = pd.DataFrame({'one': [10, 20, 30, 40, 50, 2000], 'two': [1000, 0, 30, 40, 50, 60]})
print("df2:")
print(df2)
print()

# DataFrame replace
print("DataFrame replace:")
print(df2.replace({1000: 10, 2000: 60}))
print()
