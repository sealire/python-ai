import pandas as pd

# 时间函数

print("datetime.now:")
print("datetime:", pd.datetime.now())
print()

print("date_range:")
print(pd.date_range('2020/11/21', periods=5))
print()

print("date_range 2:")
print(pd.date_range('2020/11/21', periods=5, freq='M'))
print()

print("bdate_range:")
print(pd.bdate_range('2020/11/21', periods=5))
print()

print("date_range 3:")
print(pd.date_range('2020/11/21', periods=5, freq='H'))
print()

print("Timedelta:")
print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
print()

print("Timedelta 2:")
print(pd.Timedelta(6, unit='h'))
print()

print("Timedelta 3:")
print(pd.Timedelta(days=2))
print()

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=td))

print("df:")
print(df)
print()

df['C'] = df['A'] + df['B']
print("df:")
print(df)
print()

df['D'] = df['C'] - df['B']
print("df:")
print(df)
print()
