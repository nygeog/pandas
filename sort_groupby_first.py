df = df.sort(['name','date', 'hour'], ascending=[1, 1, 1])
dfg = df.groupby(['name','date', 'hour']).first().reset_index()
