import numpy as np

def randIntForRow(idx):
	return np.random.randint(0,100)

df['rando'] = df.INDEX.map(randIntForRow)

#INDEX could be just any row, just helps w/ apply 