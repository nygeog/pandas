df_list = []

for j in all_csvs:

	df = pd.read_csv(j, header=0, dtype={'state':object,'county':object,'tract':object})
	df_list.append(df)

df = pd.concat(df_list)
