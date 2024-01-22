#remove repeated data in pandas

import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 8, 8]})
# print(df)

print(df.loc[df['A'].shift() != df['A']])