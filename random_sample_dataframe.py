import pandas as pd
import random

df = pd.read_csv('superbowl_test.csv')

sample_pct = 0.1
count_pct = int(round(len(df.index) * sample_pct))

rows = random.sample(df.index, count_pct)
df_10 = df.ix[rows]
df_90 = df.drop(rows)

df_10.to_csv('superbowl_test_sample.csv',index=False)

#http://stackoverflow.com/questions/12190874/pandas-sampling-a-dataframe
