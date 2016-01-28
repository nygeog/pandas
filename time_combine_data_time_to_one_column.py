#http://stackoverflow.com/questions/17978092/combine-date-and-time-columns-using-python-pandas

df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
