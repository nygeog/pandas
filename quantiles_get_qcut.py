df1prodQuantiles = pd.qcut(df1['production'], 10).value_counts()
print 'CORN', df1prodQuantiles
df2prodQuantiles = pd.qcut(df2['production'], 10).value_counts()
print 'SOY',  df2prodQuantiles

#http://stackoverflow.com/questions/30211923/what-is-the-difference-between-pandas-qcut-and-pandas-cut