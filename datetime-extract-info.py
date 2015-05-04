df['year'] = pd.DatetimeIndex(df['ArrivalDate']).year
df['month'] = pd.DatetimeIndex(df['ArrivalDate']).month

#or...

df['year'] = df['ArrivalDate'].dt.year
df['month'] = df['ArrivalDate'].dt.month


#from http://stackoverflow.com/questions/25146121/extracting-just-month-and-year-from-pandas-datetime-column-python