#http://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column


df['color'] = np.where(df['Set']=='Z', 'green', 'red')
#For example,

import pandas as pd
import numpy as np

df = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
df['color'] = np.where(df['Set']=='Z', 'green', 'red')
print(df)

#yields

  Set Type  color
0   Z    A  green
1   Z    B  green
2   X    B    red
3   Y    C    red