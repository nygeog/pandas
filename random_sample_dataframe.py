rows = random.sample(df.index, 10)
df_10 = df.ix[rows]
df_90 = df.drop(rows)

#http://stackoverflow.com/questions/12190874/pandas-sampling-a-dataframe
