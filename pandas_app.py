import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2020', periods=10),
                  columns=['A', 'B', 'C', 'D'])
print(df)
print(df.rolling(window=4).mean())
