import pandas as pd
import numpy as np

# 分组函数

ipl_data = {
    'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'kings', 'Kings', 'Kings',
             'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
    'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
    'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print("df:")
print(df)
print()

# DataFrame groupby
print("DataFrame groupby:")
grouped = df.groupby('Team')
print(grouped.groups)
for name, group in grouped:
    print(name)
    print(group)
print()

# DataFrame get_group
print("DataFrame get_group:")
print(grouped.get_group('Riders'))
print()

# DataFrame agg
print("DataFrame agg:")
print(grouped['Points'].agg(np.mean))
print()

# DataFrame agg 2
print("DataFrame agg 2:")
print(grouped.agg(np.size))
print()

# DataFrame agg 3
print("DataFrame agg 3:")
print(grouped['Points'].agg([np.sum, np.mean, np.std]))
print()

# DataFrame transform
print("DataFrame transform:")
score = lambda x: (x - x.mean()) / x.std() * 10
print(grouped.transform(score))
print()

# DataFrame groupby 4
print("DataFrame groupby 4:")
print(grouped.groups)
filter = df.groupby('Team').filter(lambda x: len(x) >= 3)
print(filter)

# DataFrame groupby 2
print("DataFrame groupby 2:")
print(df.groupby(['Team', 'Year']).groups)
print()

