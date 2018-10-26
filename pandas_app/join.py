import pandas as pd

# 合并连接函数

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']})
df2 = pd.DataFrame(
    {'id': [1, 2, 3, 4, 5],
     'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
     'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']})
print("df1:")
print(df1)
print("df2")
print(df2)

# DataFrame inner join
print("DataFrame inner join:")
print(pd.merge(df1, df2, on='id'))
print()

# DataFrame inner join 2
print("DataFrame inner join 2:")
print(pd.merge(df1, df2, on=['id', 'subject_id']))
print()

# DataFrame inner join 3
print("DataFrame inner join 3:")
print(pd.merge(df1, df2, on='subject_id', how='left'))
print()

# DataFrame inner join 4
print("DataFrame inner join 4:")
print(pd.merge(df1, df2, on='subject_id', how='right'))
print()

# DataFrame inner join 5
print("DataFrame inner join 5:")
print(pd.merge(df1, df2, on='subject_id', how='outer'))
print()
