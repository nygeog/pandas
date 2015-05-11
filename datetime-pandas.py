#create date and time from datetime field. 

ioCSV = '/Users/danielmsheehan/GIS/rio/tasks/201505_gpx_files/data/input/subjects/csv/split/s20150412_358_15779.csv'
df = pd.read_csv(ioCSV)
df['datetime'] = df['datetime'].astype('datetime64[ns]')
df['date']     = df['datetime'].map(lambda x: x.strftime('%Y-%m-%d'))
df['time']     = df['datetime'].map(lambda x: x.strftime('%X'))
df['day']      = df['datetime'].map(lambda x: x.strftime('%a'))
#df['uid']  = df  
df.head(10)