import pandas as pd
import numpy as np

# 窗口函数

s = pd.Series([1, 2, 3, 5, 6, 10, 12, 14, 12, 30])
print("s:", s)
print()

# Series rolling
print("Series rolling:")
print(s.rolling(window=3).mean())
print()

# Series expanding
print("Series expanding:")
print(s.expanding(min_periods=4).sum())
print()

# Series ewm
print("Series ewm:")
print(s.ewm(com=0.5).mean())
print()

df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2020', periods=10),
                  columns=['A', 'B', 'C', 'D'])
print("df:")
print(df)
print()

# DataFrame rolling
print("DataFrame rolling:")
print(df.rolling(window=3).mean())
print()

# DataFrame expanding
print("DataFrame expanding:")
print(df.expanding(min_periods=4).sum())
print()

# DataFrame ewm
print("DataFrame ewm:")
print(df.ewm(com=0.5).mean())
print()
