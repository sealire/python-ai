import pandas as pd

# 级联函数

df1 = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5'],
    'Marks_scored': [98, 90, 87, 69, 78]},
    index=[1, 2, 3, 4, 5])
df2 = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5'],
    'Marks_scored': [89, 80, 79, 97, 88]},
    index=[1, 2, 3, 4, 5])

print("df1:")
print(df1)
print("df2:")
print(df2)

# DataFrame concat
print("DataFrame concat:")
print(pd.concat([df1, df2]))
print()

# DataFrame concat 2
print("DataFrame concat 2:")
print(pd.concat([df1, df2], keys=['x', 'y']))
print()

# DataFrame concat 3
print("DataFrame concat 3:")
print(pd.concat([df1, df2], keys=['x', 'y'], ignore_index=True))
print()

# DataFrame concat 4
print("DataFrame concat 4:")
print(pd.concat([df1, df2], axis=1))
print()

# DataFrame concat 5
print("DataFrame concat 5:")
print(df1.append(df2))
print()

# DataFrame concat 6
print("DataFrame concat 7:")
print(df1.append([df1, df2, df1]))
print()
