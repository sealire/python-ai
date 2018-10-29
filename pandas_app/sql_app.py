import pandas as pd

# sql函数

url = 'tips.csv'

tips = pd.read_csv(url)
print("tips:")
print(tips.head())
print()

rs = tips[['total_bill', 'tip', 'smoker', 'time']].head(5)
print("tips 2:")
print(rs)
print()

rs = tips[tips['sex'] == 'Female'].head(5)
print("tips 3:")
print(rs)
print()

rs = tips.groupby('sex').size()
print("tips 4:")
print(rs)
print()
