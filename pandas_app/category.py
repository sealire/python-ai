import pandas as pd
import numpy as np

# 分类函数

s = pd.Series(["a", "b", "c", "a"], dtype="category")
print("category:")
print(s)
print()

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print("Categorical:")
print(cat)
print()

cat = cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'])
print("Categorical 2:")
print(cat)
print()

cat = cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'], ordered=True)
print("Categorical 3:")
print(cat)
print()

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat": cat, "s": ["a", "c", "c", np.nan]})
print("Categorical 4:")
print(df.describe())
print()
print(df["cat"].describe())
print()

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print("categories:")
print(s.categories)
print()

print("ordered:")
print(s.ordered)
print()

s = pd.Series(["a", "b", "c", "a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]
print("categories 2:")
print(s.cat.categories)
print()

s = pd.Series(["a", "b", "c", "a"], dtype="category")
s = s.cat.add_categories([4])
print("add_categories:")
print(s.cat.categories)
print()

s = pd.Series(["a", "b", "c", "a"], dtype="category")
print("remove_categories:")
print(s.cat.remove_categories("a"))
print()
