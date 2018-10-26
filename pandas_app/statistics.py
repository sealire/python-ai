import pandas as pd
import numpy as np

# 统计函数

s = pd.Series([1, 2, 3, 4, 5, 4])
print("s:")
print(s)
print()

# series比较 每个元素与其前一个元素进行比较
print("series比较，与前一元素比较：")
print(s.pct_change())
print()

df = pd.DataFrame(np.random.randn(5, 2))
print("df:")
print(df)
print()

# DataFrame列比较 每个元素与其前一个元素进行比较
print("DataFrame列比较，与前一元素比较：")
print(df.pct_change())
print()

# DataFrame行比较 每个元素与其前一个元素进行比较
print("DataFrame行比较，与前一元素比较：")
print(df.pct_change(axis=1))
print()

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print("s1:")
print(s1)
print()
print("s2:")
print(s2)
print()

# series协方差
print("series协方差：", s1.cov(s2))
print()

df1 = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print("df1:")
print(df1)
print()

# DataFrame协方差
print("DataFrame协方差:")
print(df1.cov())
print()

# series相关性
print("series相关性:", s1.corr(s2))
print("series相关性:", s1.corr(s1))
print()

# DataFrame相关性
print("DataFrame相关性:")
print(print(df1.corr()))
print()

s3 = pd.Series(np.random.np.random.randn(10), index=list('abcdefghij'))
s3['d'] = s3['b']
s3['a'] = s3['e'] = s3['g']
print("s3:")
print(s3)
print()

# series排名
print("series排名:")
print(s3.rank())
print(s3.rank(method='min'))
print()
