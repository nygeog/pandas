import pandas as pd

df = pd.DataFrame([[1, 3], [2, 4]], columns=['A', 'B'])

df2 = pd.DataFrame([[1, 5], [1, 6]], columns=['A', 'C'])


print df.head(10)
print df2.head(10)

df = df.merge(df2, how='left')#, on='A')  # merges on columns A

print df.head(10)