def sidewalkPresent(x): 
	if x == 'No': 
		return 1 
	elif x == 'Yes, sidewalks present but uneven or disrupted': 
		return 0.5 
	else: 
		return 0 

df['Rsidewalk'] = df.sidewalk_present.map(sidewalkPresent)