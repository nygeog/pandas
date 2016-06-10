from _settings import *

wd = dg

wi = do+'input/' #osrm
wo = wd+'output/'
wp = wd+'processing/'

df = pd.read_csv(wp+'paratransit_cb2010_pd_pairs.csv')

print df.head(10)

def save_df(df, chunk_size=50000):
	df_size = len(df.index)
	print df_size
	for i, start in enumerate(range(0, df_size, chunk_size)):
		df[start:start+chunk_size].to_csv(wi+'paratransit_cb_pd_pairs_{}.csv'.format(i),index=False)

save_df(df,chunk_size=50000)

#http://stackoverflow.com/questions/35001645/splitting-a-pandas-data-frame-into-rows-by-count